"""
Domain-Klasse für eine Prüfungsleistung.
"""

from dataclasses import dataclass

from .enums import Pruefungsart


@dataclass
class Pruefungsleistung:
    """
    Repräsentiert eine Prüfungsleistung eines Moduls.

    Attributes:
        id: Eindeutige ID der Prüfungsleistung in der SQLite-Datenbank.
        art: Art der Prüfungsleistung.
        bezeichnung: Bezeichnung der Prüfungsleistung.
    """

    id: int
    art: Pruefungsart
    bezeichnung: str
