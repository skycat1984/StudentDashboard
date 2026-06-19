"""
Domain-Klasse für einen Studiengang.
"""

from dataclasses import dataclass, field

from .enums import Abschluss
from .semester import Semester


@dataclass
class Studiengang:
    """
    Repräsentiert einen Studiengang mit seinen Semestern.

    Attributes:
        id: Eindeutige ID des Studiengangs in der SQLite-Datenbank.
        name: Bezeichnung des Studiengangs.
        abschluss: Angestrebter akademischer Abschluss.
        gesamt_ects: Gesamtzahl der für den Studiengang vorgesehenen ECTS.
        semester: Dem Studiengang zugeordnete Semester.
    """

    id: int
    name: str
    abschluss: Abschluss
    gesamt_ects: int
    semester: list[Semester] = field(default_factory=list)

