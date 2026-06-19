"""
DTO zur Übertragung der aufbereiteten Dashboard-Daten.

Das DashboardDatenDTO bündelt die vom Controller zusammengestellten
Kennzahlen und Modullisten für die Übergabe an die View.
"""

from dataclasses import dataclass
from datetime import date

from ..domain.modul import Modul


@dataclass
class DashboardDatenDTO:
    """
    Enthält alle für die Darstellung des Dashboards benötigten Daten.

    Attributes:
        erreichte_ects:
            Summe der ECTS aller abgeschlossenen Module.
        gesamt_ects:
            Gesamtzahl der für den Studienabschluss erforderlichen ECTS.
        ects_fortschritt:
            Anteil der bereits erreichten ECTS in Prozent.
        zeitfortschritt:
            Anteil der bereits verbrauchten Studienzeit in Prozent.
        notendurchschnitt:
            Durchschnitt der bestandenen Prüfungen.
        abschlussprognose:
            Prognostiziertes Datum des Studienabschlusses.
        studienstatus:
            Bewertung des Studienverlaufs, beispielsweise
            „Im Zeitplan“ oder „Hinter dem Zeitplan“.
        bestandene_module:
            Bereits abgeschlossene Module.
        offene_module:
            Noch nicht belegte Module des Studienplans.
        aktuelle_module:
            Derzeit gebuchte Module.
    """

    erreichte_ects: int
    gesamt_ects: int
    ects_fortschritt: float
    zeitfortschritt: float
    notendurchschnitt: float
    abschlussprognose: date
    studienstatus: str
    bestandene_module: list[Modul]
    offene_module: list[Modul]
    aktuelle_module: list[Modul]