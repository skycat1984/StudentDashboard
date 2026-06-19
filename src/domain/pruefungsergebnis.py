"""
Domain-Klasse für das Ergebnis einer Prüfungsleistung.
"""

from dataclasses import dataclass
from datetime import date

from .enums import Pruefungsstatus
from .pruefungsleistung import Pruefungsleistung


@dataclass
class Pruefungsergebnis:
    """
    Repräsentiert das Prüfungsergebnis eines Studenten.

    Attributes:
        id: Eindeutige ID des Prüfungsergebnisses in der SQLite-Datenbank.
        pruefungsleistung: Zugehörige Prüfungsleistung.
        status: Aktueller Status des Prüfungsergebnisses.
        note: Erreichte Note oder None, solange noch keine Bewertung vorliegt.
        pruefungsdatum: Datum der Prüfung oder None, wenn noch kein Datum
            vorhanden ist.
    """

    id: int
    pruefungsleistung: Pruefungsleistung
    status: Pruefungsstatus
    note: float | None = None
    pruefungsdatum: date | None = None

