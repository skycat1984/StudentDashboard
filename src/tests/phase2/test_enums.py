from enum import Enum


class Studienmodell(Enum):
    VOLLZEIT = "Vollzeit"
    TEILZEIT_I = "Teilzeit I"
    TEILZEIT_II = "Teilzeit II"


class Abschluss(Enum):
    BACHELOR = "Bachelor"
    MASTER = "Master"


class Pruefungsart(Enum):
    KLAUSUR = "Klausur"
    PORTFOLIO = "Portfolio"
    HAUSARBEIT = "Hausarbeit"
    PROJEKTARBEIT = "Projektarbeit"
    FACHPRASENTATION = "Fachpräsentation"


class Belegungsstatus(Enum):
    GEBUCHT = "Gebucht"
    ABGESCHLOSSEN = "Abgeschlossen"


class Pruefungsstatus(Enum):
    OFFEN = "Offen"
    BESTANDEN = "Bestanden"
    NICHT_BESTANDEN = "Nicht bestanden"


# Testausgaben

print("Studienmodell:")
print(Studienmodell.VOLLZEIT)
print(Studienmodell.VOLLZEIT.value)

print("\nAbschluss:")
print(Abschluss.BACHELOR)

print("\nPrüfungsart:")
for art in Pruefungsart:
    print("-", art.value)

print("\nBelegungsstatus:")
print(Belegungsstatus.ABGESCHLOSSEN.value)

print("\nPrüfungsstatus:")
print(Pruefungsstatus.BESTANDEN.value)