"""
Testprogramm zu Properties, Polymorphie und Duck Typing.

Die Beispiele beziehen sich auf das Studien-Dashboard, gehören aber
nicht zwingend zur späteren Produktivimplementierung.
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# 1. Properties
# ---------------------------------------------------------

class Pruefungsergebnis:
    """Demonstriert einen kontrollierten Attributzugriff über eine Property."""

    def __init__(self, note: float) -> None:
        self.note = note

    @property
    def note(self) -> float:
        """Getter: Gibt die gespeicherte Note zurück."""
        return self._note

    @note.setter
    def note(self, wert: float) -> None:
        """Setter: Prüft die Note vor dem Speichern."""
        if not 1.0 <= wert <= 5.0:
            raise ValueError("Die Note muss zwischen 1,0 und 5,0 liegen.")

        self._note = wert


# ---------------------------------------------------------
# 2. Polymorphie über Vererbung
# ---------------------------------------------------------

class Pruefungsleistung(ABC):
    """Abstrakte Oberklasse für verschiedene Prüfungsleistungen."""

    @abstractmethod
    def beschreibung(self) -> str:
        """Muss von jeder Unterklasse implementiert werden."""
        pass


class Klausur(Pruefungsleistung):
    """Konkrete Prüfungsleistung Klausur."""

    def beschreibung(self) -> str:
        return "Schriftliche Klausur"


class Projekt(Pruefungsleistung):
    """Konkrete Prüfungsleistung Projekt."""

    def beschreibung(self) -> str:
        return "Praktisches Projekt"


def zeige_pruefungsleistung(leistung: Pruefungsleistung) -> None:
    """Verwendet unterschiedliche Unterklassen über dieselbe Methode."""
    print(leistung.beschreibung())


# ---------------------------------------------------------
# 3. Duck Typing
# ---------------------------------------------------------

class SQLiteModulRepository:
    """Lädt Module aus einer SQLite-Datenbank."""

    def lade_alle(self) -> list[str]:
        return ["Programmierung", "Datenbanken"]


class TestModulRepository:
    """Stellt Testdaten ohne Datenbank bereit."""

    def lade_alle(self) -> list[str]:
        return ["Testmodul 1", "Testmodul 2"]


class DashboardController:
    """Verwendet jedes Repository, das lade_alle() bereitstellt."""

    def __init__(self, repository) -> None:
        self.repository = repository

    def lade_module(self) -> list[str]:
        return self.repository.lade_alle()


def main() -> None:
    """Führt die Tests zu den drei Konzepten aus."""

    print("1. Property")
    ergebnis = Pruefungsergebnis(2.0)
    print(f"Gespeicherte Note: {ergebnis.note}")

    try:
        ergebnis.note = 7.0
    except ValueError as fehler:
        print(f"Fehler: {fehler}")

    print("\n2. Polymorphie")
    pruefungsleistungen = [Klausur(), Projekt()]

    for leistung in pruefungsleistungen:
        zeige_pruefungsleistung(leistung)

    print("\n3. Duck Typing")
    sqlite_controller = DashboardController(SQLiteModulRepository())
    print(sqlite_controller.lade_module())

    test_controller = DashboardController(TestModulRepository())
    print(test_controller.lade_module())


if __name__ == "__main__":
    main()
