"""
Domain-Klasse für einen Studenten.
"""

from dataclasses import dataclass, field
from datetime import date

from .enums import Studienmodell
from .modulbelegung import Modulbelegung
from .pruefungsergebnis import Pruefungsergebnis
from .studiengang import Studiengang


@dataclass
class Student:
    """
    Repräsentiert einen Studenten mit seinem Studiengang und Studienfortschritt.

    Attributes:
        id: Eindeutige ID des Studenten in der SQLite-Datenbank.
        matrikelnummer: Eindeutige Matrikelnummer des Studenten.
        name: Name des Studenten.
        startdatum: Datum des Studienbeginns.
        studienmodell: Gewähltes Zeitmodell des Studiums.
        studiengang: Zugeordneter Studiengang oder None, falls noch keine
            Zuordnung vorhanden ist.
        modulbelegungen: Vom Studenten gebuchte oder abgeschlossene Module.
        pruefungsergebnisse: Prüfungsergebnisse des Studenten.
    """

    id: int
    matrikelnummer: str
    name: str
    startdatum: date
    studienmodell: Studienmodell
    studiengang: Studiengang
    modulbelegungen: list[Modulbelegung] = field(default_factory=list)
    pruefungsergebnisse: list[Pruefungsergebnis] = field(default_factory=list)
