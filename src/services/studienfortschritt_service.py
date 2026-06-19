"""
Service zur Berechnung des individuellen Studienfortschritts.

Der Service verarbeitet Domain-Objekte und enthält keine Datenbankzugriffe
oder Darstellungslogik.
"""

from ..domain.enums import Belegungsstatus
from ..domain.modul import Modul
from ..domain.modulbelegung import Modulbelegung


class StudienfortschrittService:
    """Berechnet ECTS-Fortschritt und gruppiert Module nach ihrem Status."""

    def berechne_ects_fortschritt(
        self,
        modulbelegungen: list[Modulbelegung],
        gesamt_ects: int,
    ) -> float:
        """
        Berechnet den prozentualen ECTS-Fortschritt.

        Berücksichtigt werden nur Modulbelegungen mit dem Status
        ABGESCHLOSSEN.

        Args:
            modulbelegungen:
                Modulbelegungen des Studenten.
            gesamt_ects:
                Gesamtzahl der für den Studienabschluss erforderlichen ECTS.

        Returns:
            Prozentualer ECTS-Fortschritt, gerundet auf zwei Nachkommastellen.

        Raises:
            ValueError:
                Wenn gesamt_ects kleiner oder gleich null ist.
        """

        if gesamt_ects <= 0:
            raise ValueError(
                "Die Gesamtzahl der ECTS muss größer als null sein."
            )

        abgeschlossene_module = self.ermittle_bestandene_module(
            modulbelegungen
        )

        erreichte_ects = sum(
            modul.ects for modul in abgeschlossene_module
        )

        fortschritt = erreichte_ects / gesamt_ects * 100

        return round(fortschritt, 2)

    def ermittle_bestandene_module(
        self,
        modulbelegungen: list[Modulbelegung],
    ) -> list[Modul]:
        """
        Ermittelt alle abgeschlossenen Module.

        Args:
            modulbelegungen:
                Modulbelegungen des Studenten.

        Returns:
            Module mit dem Belegungsstatus ABGESCHLOSSEN.
        """

        return [
            belegung.modul
            for belegung in modulbelegungen
            if belegung.status == Belegungsstatus.ABGESCHLOSSEN
        ]

    def ermittle_aktuelle_module(
        self,
        modulbelegungen: list[Modulbelegung],
    ) -> list[Modul]:
        """
        Ermittelt alle derzeit gebuchten Module.

        Args:
            modulbelegungen:
                Modulbelegungen des Studenten.

        Returns:
            Module mit dem Belegungsstatus GEBUCHT.
        """

        return [
            belegung.modul
            for belegung in modulbelegungen
            if belegung.status == Belegungsstatus.GEBUCHT
        ]

    def ermittle_offene_module(
        self,
        alle_module: list[Modul],
        modulbelegungen: list[Modulbelegung],
    ) -> list[Modul]:
        """
        Ermittelt alle noch nicht belegten Module des Studienplans.

        Ein Modul gilt als offen, wenn dafür weder eine gebuchte noch eine
        abgeschlossene Modulbelegung vorhanden ist.

        Args:
            alle_module:
                Alle Module des zum Studienmodell passenden Studienplans.
            modulbelegungen:
                Modulbelegungen des Studenten.

        Returns:
            Noch nicht belegte Module.
        """

        belegte_modul_ids = {
            belegung.modul.id
            for belegung in modulbelegungen
        }

        return [
            modul
            for modul in self._eindeutige_module(alle_module)
            if modul.id not in belegte_modul_ids
        ]

    @staticmethod
    def _eindeutige_module(module: list[Modul]) -> list[Modul]:
        """
        Entfernt doppelte Module anhand ihrer Datenbank-ID.

        Die ursprüngliche Reihenfolge der Module bleibt erhalten.
        """

        module_nach_id: dict[int, Modul] = {}

        for modul in module:
            module_nach_id.setdefault(modul.id, modul)

        return list(module_nach_id.values())

