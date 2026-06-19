"""
Domain-Klasse für ein Studienmodul.
"""

from dataclasses import dataclass, field

from .pruefungsleistung import Pruefungsleistung


@dataclass
class Modul:
    """
    Repräsentiert ein Modul innerhalb des Studienplans.

    Attributes:
        id: Eindeutige ID des Moduls in der SQLite-Datenbank.
        titel: Bezeichnung des Moduls.
        ects: Anzahl der für das Modul vorgesehenen ECTS-Punkte.
        pruefungsleistungen: Dem Modul zugeordnete Prüfungsleistungen.
    """

    id: int
    titel: str
    ects: int
    pruefungsleistungen: list[Pruefungsleistung] = field(default_factory=list)
