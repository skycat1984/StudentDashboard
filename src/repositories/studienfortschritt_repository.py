"""
Repository zum Laden des individuellen Studienfortschritts.

Das Repository liest Modulbelegungen und Prüfungsergebnisse aus der
SQLite-Datenbank und verknüpft sie mit bereits geladenen Domain-Objekten.
"""

from datetime import date

from .database import datenbankverbindung
from ..domain.enums import Belegungsstatus, Pruefungsstatus
from ..domain.modul import Modul
from ..domain.modulbelegung import Modulbelegung
from ..domain.pruefungsergebnis import Pruefungsergebnis
from ..domain.pruefungsleistung import Pruefungsleistung


class StudienfortschrittRepository:
    """Lädt Modulbelegungen und Prüfungsergebnisse eines Studenten."""

    def lade_modulbelegungen(
        self,
        student_id: int,
        module_nach_id: dict[int, Modul],
    ) -> list[Modulbelegung]:
        """
        Lädt alle Modulbelegungen eines Studenten.

        Args:
            student_id:
                ID des Studenten.
            module_nach_id:
                Bereits geladene Module, geordnet nach ihrer Datenbank-ID.

        Returns:
            Liste der Modulbelegungen des Studenten.

        Raises:
            LookupError:
                Wenn eine Modulbelegung auf ein nicht geladenes Modul verweist.
        """

        with datenbankverbindung() as connection:
            datensaetze = connection.execute(
                """
                SELECT
                    id,
                    modul_id,
                    status,
                    buchungsdatum,
                    abgeschlossen_am
                FROM modulbelegung
                WHERE student_id = ?
                ORDER BY buchungsdatum, id
                """,
                (student_id,),
            ).fetchall()

        modulbelegungen: list[Modulbelegung] = []

        for datensatz in datensaetze:
            modul_id = datensatz["modul_id"]
            modul = module_nach_id.get(modul_id)

            if modul is None:
                raise LookupError(
                    "Das Modul der Modulbelegung wurde im Studienplan "
                    f"nicht gefunden. Modul-ID: {modul_id}"
                )

            modulbelegungen.append(
                Modulbelegung(
                    id=datensatz["id"],
                    modul=modul,
                    status=Belegungsstatus(datensatz["status"]),
                    buchungsdatum=date.fromisoformat(
                        datensatz["buchungsdatum"]
                    ),
                    abgeschlossen_am=self._datum_oder_none(
                        datensatz["abgeschlossen_am"]
                    ),
                )
            )

        return modulbelegungen

    def lade_pruefungsergebnisse(
        self,
        student_id: int,
        pruefungsleistungen_nach_id: dict[int, Pruefungsleistung],
    ) -> list[Pruefungsergebnis]:
        """
        Lädt alle Prüfungsergebnisse eines Studenten.

        Args:
            student_id:
                ID des Studenten.
            pruefungsleistungen_nach_id:
                Bereits geladene Prüfungsleistungen, geordnet nach ihrer
                Datenbank-ID.

        Returns:
            Liste der Prüfungsergebnisse des Studenten.

        Raises:
            LookupError:
                Wenn ein Ergebnis auf eine nicht geladene Prüfungsleistung
                verweist.
        """

        with datenbankverbindung() as connection:
            datensaetze = connection.execute(
                """
                SELECT
                    id,
                    pruefungsleistung_id,
                    status,
                    note,
                    pruefungsdatum
                FROM pruefungsergebnis
                WHERE student_id = ?
                ORDER BY pruefungsdatum, id
                """,
                (student_id,),
            ).fetchall()

        pruefungsergebnisse: list[Pruefungsergebnis] = []

        for datensatz in datensaetze:
            pruefungsleistung_id = datensatz["pruefungsleistung_id"]

            pruefungsleistung = pruefungsleistungen_nach_id.get(
                pruefungsleistung_id
            )

            if pruefungsleistung is None:
                raise LookupError(
                    "Die Prüfungsleistung des Prüfungsergebnisses wurde "
                    "im Studienplan nicht gefunden. "
                    f"Prüfungsleistungs-ID: {pruefungsleistung_id}"
                )

            pruefungsergebnisse.append(
                Pruefungsergebnis(
                    id=datensatz["id"],
                    pruefungsleistung=pruefungsleistung,
                    status=Pruefungsstatus(datensatz["status"]),
                    note=datensatz["note"],
                    pruefungsdatum=self._datum_oder_none(
                        datensatz["pruefungsdatum"]
                    ),
                )
            )

        return pruefungsergebnisse

    @staticmethod
    def _datum_oder_none(wert: str | None) -> date | None:
        """
        Wandelt einen ISO-Datumswert in ein date-Objekt um.

        Args:
            wert:
                Datum im Format YYYY-MM-DD oder None.

        Returns:
            Das umgewandelte Datum oder None.
        """

        if wert is None:
            return None

        return date.fromisoformat(wert)

