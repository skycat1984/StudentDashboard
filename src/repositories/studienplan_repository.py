"""
Repository zum Laden des Studienplans.

Das Repository liest Semester, Module und Prüfungsleistungen aus der
SQLite-Datenbank und erzeugt daraus zusammenhängende Domain-Objekte.
"""

import sqlite3

from .database import datenbankverbindung
from ..domain.enums import Pruefungsart, Studienmodell
from ..domain.modul import Modul
from ..domain.pruefungsleistung import Pruefungsleistung
from ..domain.semester import Semester


class StudienplanRepository:
    """Lädt Semester, Module und Prüfungsleistungen des Studienplans."""

    def lade_semester(
        self,
        studiengang_id: int,
        studienmodell: Studienmodell,
    ) -> list[Semester]:
        """
        Lädt alle Semester eines Studiengangs für ein bestimmtes Studienmodell.

        Die zugehörigen Module und Prüfungsleistungen werden ebenfalls geladen.

        Args:
            studiengang_id:
                ID des Studiengangs.
            studienmodell:
                Studienmodell, für das der Studienplan geladen wird.

        Returns:
            Semester einschließlich der zugeordneten Module und
            Prüfungsleistungen.
        """

        with datenbankverbindung() as connection:
            return self._lade_semester_mit_verbindung(
                connection=connection,
                studiengang_id=studiengang_id,
                studienmodell=studienmodell,
            )

    def lade_module(self, semester_id: int) -> list[Modul]:
        """
        Lädt alle Module eines Semesters.

        Die zugehörigen Prüfungsleistungen werden ebenfalls geladen.

        Args:
            semester_id:
                ID des Semesters.

        Returns:
            Module des Semesters einschließlich ihrer Prüfungsleistungen.
        """

        with datenbankverbindung() as connection:
            return self._lade_module_mit_verbindung(
                connection=connection,
                semester_id=semester_id,
            )

    def lade_pruefungsleistungen(
        self,
        modul_id: int,
    ) -> list[Pruefungsleistung]:
        """
        Lädt alle Prüfungsleistungen eines Moduls.

        Args:
            modul_id:
                ID des Moduls.

        Returns:
            Prüfungsleistungen des Moduls.
        """

        with datenbankverbindung() as connection:
            return self._lade_pruefungsleistungen_mit_verbindung(
                connection=connection,
                modul_id=modul_id,
            )

    def _lade_semester_mit_verbindung(
        self,
        connection: sqlite3.Connection,
        studiengang_id: int,
        studienmodell: Studienmodell,
    ) -> list[Semester]:
        """Lädt Semester über eine bereits geöffnete Verbindung."""

        datensaetze = connection.execute(
            """
            SELECT
                id,
                nummer,
                bezeichnung,
                zeitmodell
            FROM semester
            WHERE studiengang_id = ?
              AND zeitmodell = ?
            ORDER BY nummer
            """,
            (
                studiengang_id,
                studienmodell.value,
            ),
        ).fetchall()

        semester_liste: list[Semester] = []

        for datensatz in datensaetze:
            semester = Semester(
                id=datensatz["id"],
                nummer=datensatz["nummer"],
                bezeichnung=datensatz["bezeichnung"],
                zeitmodell=Studienmodell(datensatz["zeitmodell"]),
                module=self._lade_module_mit_verbindung(
                    connection=connection,
                    semester_id=datensatz["id"],
                ),
            )

            semester_liste.append(semester)

        return semester_liste

    def _lade_module_mit_verbindung(
        self,
        connection: sqlite3.Connection,
        semester_id: int,
    ) -> list[Modul]:
        """Lädt Module eines Semesters über eine geöffnete Verbindung."""

        datensaetze = connection.execute(
            """
            SELECT
                modul.id,
                modul.titel,
                modul.ects
            FROM semester_modul
            JOIN modul
                ON modul.id = semester_modul.modul_id
            WHERE semester_modul.semester_id = ?
            ORDER BY modul.titel
            """,
            (semester_id,),
        ).fetchall()

        modul_liste: list[Modul] = []

        for datensatz in datensaetze:
            modul = Modul(
                id=datensatz["id"],
                titel=datensatz["titel"],
                ects=datensatz["ects"],
                pruefungsleistungen=(
                    self._lade_pruefungsleistungen_mit_verbindung(
                        connection=connection,
                        modul_id=datensatz["id"],
                    )
                ),
            )

            modul_liste.append(modul)

        return modul_liste

    @staticmethod
    def _lade_pruefungsleistungen_mit_verbindung(
        connection: sqlite3.Connection,
        modul_id: int,
    ) -> list[Pruefungsleistung]:
        """Lädt Prüfungsleistungen über eine geöffnete Verbindung."""

        datensaetze = connection.execute(
            """
            SELECT
                id,
                art,
                bezeichnung
            FROM pruefungsleistung
            WHERE modul_id = ?
            ORDER BY bezeichnung
            """,
            (modul_id,),
        ).fetchall()

        return [
            Pruefungsleistung(
                id=datensatz["id"],
                art=Pruefungsart(datensatz["art"]),
                bezeichnung=datensatz["bezeichnung"],
            )
            for datensatz in datensaetze
        ]

