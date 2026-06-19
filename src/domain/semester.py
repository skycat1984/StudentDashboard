"""
Domain-Klasse für ein Studiensemester.
"""

from dataclasses import dataclass, field

from .enums import Studienmodell
from .modul import Modul


@dataclass
class Semester:
    """
    Repräsentiert ein Semester innerhalb eines Studiengangs.

    Attributes:
        id: Eindeutige ID des Semesters in der SQLite-Datenbank.
        nummer: Laufende Nummer des Semesters.
        bezeichnung: Bezeichnung des Semesters.
        zeitmodell: Studienmodell, das für das Semester gilt.
        module: Dem Semester zugeordnete Module.
    """

    id: int
    nummer: int
    bezeichnung: str
    zeitmodell: Studienmodell
    module: list[Modul] = field(default_factory=list)
