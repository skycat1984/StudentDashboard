"""
Repository zum Laden der Stammdaten des Studien-Dashboards.

Das Repository liest den Studenten und den zugehörigen Studiengang
aus der SQLite-Datenbank und erzeugt daraus Domain-Objekte.
"""

from datetime import date
import sqlite3

from .database import datenbankverbindung
from ..domain.enums import Abschluss, Studienmodell
from ..domain.student import Student
from ..domain.studiengang import Studiengang


class StammdatenRepository:
    """Lädt die grundlegenden Stammdaten des Dashboards."""

    def lade_studiengang(self) -> Studiengang:
        """
        Lädt den ersten vorhandenen Studiengang aus der Datenbank.

        Returns:
            Der geladene Studiengang.

        Raises:
            LookupError:
                Wenn kein Studiengang vorhanden ist.
        """

        with datenbankverbindung() as connection:
            datensatz = connection.execute(
                """
                SELECT
                    id,
                    name,
                    abschluss,
                    gesamt_ects
                FROM studiengang
                ORDER BY id
                LIMIT 1
                """
            ).fetchone()

        if datensatz is None:
            raise LookupError(
                "In der Datenbank wurde kein Studiengang gefunden."
            )

        return self._erstelle_studiengang(datensatz)

    def lade_student(self) -> Student:
        """
        Lädt den ersten vorhandenen Studenten mit seinem Studiengang.

        Die Modulbelegungen und Prüfungsergebnisse werden später vom
        StudienfortschrittRepository ergänzt.

        Returns:
            Der geladene Student mit zugeordnetem Studiengang.

        Raises:
            LookupError:
                Wenn kein Student oder kein zugehöriger Studiengang
                vorhanden ist.
        """

        with datenbankverbindung() as connection:
            datensatz = connection.execute(
                """
                SELECT
                    student.id AS student_id,
                    student.matrikelnummer,
                    student.name AS student_name,
                    student.startdatum,
                    student.studienmodell,

                    studiengang.id AS studiengang_id,
                    studiengang.name AS studiengang_name,
                    studiengang.abschluss,
                    studiengang.gesamt_ects
                FROM student
                JOIN studiengang
                    ON studiengang.id = student.studiengang_id
                ORDER BY student.id
                LIMIT 1
                """
            ).fetchone()

        if datensatz is None:
            raise LookupError(
                "In der Datenbank wurde kein Student mit Studiengang gefunden."
            )

        studiengang = Studiengang(
            id=datensatz["studiengang_id"],
            name=datensatz["studiengang_name"],
            abschluss=Abschluss(datensatz["abschluss"]),
            gesamt_ects=datensatz["gesamt_ects"],
        )

        return Student(
            id=datensatz["student_id"],
            matrikelnummer=datensatz["matrikelnummer"],
            name=datensatz["student_name"],
            startdatum=date.fromisoformat(datensatz["startdatum"]),
            studienmodell=Studienmodell(datensatz["studienmodell"]),
            studiengang=studiengang,
        )

    @staticmethod
    def _erstelle_studiengang(
        datensatz: sqlite3.Row,
    ) -> Studiengang:
        """
        Wandelt einen SQLite-Datensatz in ein Studiengang-Objekt um.

        Args:
            datensatz:
                Datensatz aus der Tabelle studiengang.

        Returns:
            Das erzeugte Studiengang-Objekt.
        """

        return Studiengang(
            id=datensatz["id"],
            name=datensatz["name"],
            abschluss=Abschluss(datensatz["abschluss"]),
            gesamt_ects=datensatz["gesamt_ects"],
        )
