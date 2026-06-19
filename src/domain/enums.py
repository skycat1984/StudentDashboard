"""
Enumerationen des Studien-Dashboards.

Die Enum-Klassen definieren feste fachliche Wertebereiche und verhindern,
dass ungültige Zeichenketten als Status, Studienmodell, Abschluss oder
Prüfungsart verwendet werden.
"""

from enum import StrEnum


class Studienmodell(StrEnum):
    """Mögliche Zeitmodelle eines Studiums."""

    VOLLZEIT = "Vollzeit"
    TEILZEIT_I = "Teilzeit I"
    TEILZEIT_II = "Teilzeit II"


class Abschluss(StrEnum):
    """Mögliche akademische Abschlüsse."""

    BACHELOR = "Bachelor"
    MASTER = "Master"


class Pruefungsart(StrEnum):
    """Mögliche Arten einer Prüfungsleistung."""

    KLAUSUR = "Klausur"
    WORKBOOK = "Workbook"
    PORTFOLIO = "Portfolio"
    PROJEKT = "Projekt"
    FACHPRAESENTATION = "Fachpräsentation"


class Belegungsstatus(StrEnum):
    """Mögliche Zustände einer Modulbelegung."""

    GEBUCHT = "Gebucht"
    ABGESCHLOSSEN = "Abgeschlossen"


class Pruefungsstatus(StrEnum):
    """Mögliche Zustände eines Prüfungsergebnisses."""

    OFFEN = "Offen"
    BESTANDEN = "Bestanden"
    NICHT_BESTANDEN = "Nicht bestanden"
