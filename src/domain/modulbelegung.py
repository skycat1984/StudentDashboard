"""
Domain-Klasse für die Belegung eines Moduls.
"""

from dataclasses import dataclass
from datetime import date

from .enums import Belegungsstatus
from .modul import Modul


@dataclass
class Modulbelegung:
    """
    Repräsentiert die Belegung eines Moduls durch einen Studenten.

    Attributes:
        id: Eindeutige ID der Modulbelegung in der SQLite-Datenbank.
        modul: Das belegte Modul.
        status: Aktueller Status der Modulbelegung.
        buchungsdatum: Datum, an dem das Modul gebucht wurde.
        abgeschlossen_am: Abschlussdatum des Moduls oder None,
            solange das Modul noch nicht abgeschlossen ist.
    """

    id: int
    modul: Modul
    status: Belegungsstatus
    buchungsdatum: date
    abgeschlossen_am: date | None = None
