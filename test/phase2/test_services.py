"""
Testprogramm: Service-Klassen

Ziel:
Untersuchung der Trennung von Domain-Klassen und Berechnungslogik.

Untersuchte Konzepte:
- Service-Klassen
- Berechnung von Kennzahlen
- Auswertung mehrerer Domain-Objekte
"""

from dataclasses import dataclass
from enum import Enum


# Status eines Prüfungsergebnisses
class Pruefungsstatus(Enum):
    OFFEN = "Offen"
    BESTANDEN = "Bestanden"
    NICHT_BESTANDEN = "Nicht bestanden"


# Status einer Modulbelegung
class Belegungsstatus(Enum):
    GEBUCHT = "Gebucht"
    ABGESCHLOSSEN = "Abgeschlossen"


# Modul
@dataclass
class Modul:
    titel: str
    ects: int


# Belegung eines Moduls
@dataclass
class Modulbelegung:
    modul: Modul
    status: Belegungsstatus


# Ergebnis einer Prüfung
@dataclass
class Pruefungsergebnis:
    modul: Modul
    note: float
    status: Pruefungsstatus


# Service zur Berechnung des Studienfortschritts
class StudienfortschrittService:
    def berechne_ects_fortschritt(
            self,
            belegungen: list[Modulbelegung],
            gesamt_ects: int
    ) -> float:
        erreichte_ects = 0

        for belegung in belegungen:
            if belegung.status == Belegungsstatus.ABGESCHLOSSEN:
                erreichte_ects += belegung.modul.ects

        return erreichte_ects / gesamt_ects * 100


# Service zur Berechnung des Notendurchschnitts
class NotenService:
    def berechne_notendurchschnitt(
            self,
            ergebnisse: list[Pruefungsergebnis]
    ) -> float:
        bestandene_pruefungen = []

        for ergebnis in ergebnisse:
            if ergebnis.status == Pruefungsstatus.BESTANDEN:
                bestandene_pruefungen.append(ergebnis)

        notensumme = 0

        for ergebnis in bestandene_pruefungen:
            notensumme += ergebnis.note

        return notensumme / len(bestandene_pruefungen)


# Testdaten erzeugen
python = Modul(
    "Objektorientierte Programmierung mit Python",
    5
)

datenbanken = Modul(
    "Datenbanken",
    5
)

projekt = Modul(
    "Projekt Software Development",
    10
)

belegungen = [
    Modulbelegung(
        python,
        Belegungsstatus.ABGESCHLOSSEN
    ),
    Modulbelegung(
        datenbanken,
        Belegungsstatus.ABGESCHLOSSEN
    ),
    Modulbelegung(
        projekt,
        Belegungsstatus.GEBUCHT
    ),
]

pruefungsergebnisse = [
    Pruefungsergebnis(
        python,
        1.7,
        Pruefungsstatus.BESTANDEN
    ),
    Pruefungsergebnis(
        datenbanken,
        2.0,
        Pruefungsstatus.BESTANDEN
    ),
]

# Services erzeugen
studienfortschritt_service = StudienfortschrittService()
noten_service = NotenService()

# Kennzahlen berechnen
ects_fortschritt = (
    studienfortschritt_service
    .berechne_ects_fortschritt(belegungen, 20)
)

notendurchschnitt = (
    noten_service
    .berechne_notendurchschnitt(pruefungsergebnisse)
)

# Ergebnisse ausgeben
print(f"ECTS-Fortschritt: {ects_fortschritt:.1f} %")
print(f"Notendurchschnitt: {notendurchschnitt:.2f}")