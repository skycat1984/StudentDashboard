"""
Controller zur Koordination des Studien-Dashboards.

Der DashboardController verbindet Repository-, Service- und DTO-Schicht.
Er lädt die benötigten Domain-Objekte, ruft die fachlichen Services auf
und stellt die Ergebnisse als DashboardDatenDTO bereit.
"""

from ..domain.modul import Modul
from ..domain.pruefungsleistung import Pruefungsleistung
from ..domain.semester import Semester
from ..dto.dashboard_daten_dto import DashboardDatenDTO
from ..repositories.stammdaten_repository import StammdatenRepository
from ..repositories.studienfortschritt_repository import (
    StudienfortschrittRepository,
)
from ..repositories.studienplan_repository import StudienplanRepository
from ..services.abschlussprognose_service import AbschlussPrognoseService
from ..services.noten_service import NotenService
from ..services.studienfortschritt_service import StudienfortschrittService


class DashboardController:
    """
    Koordiniert das Laden, Verarbeiten und Aufbereiten der Dashboard-Daten.

    Die benötigten Repositories und Services werden über den Konstruktor
    übergeben. Dadurch bleibt der Controller unabhängig von ihrer konkreten
    Erzeugung.
    """

    def __init__(
        self,
        stammdaten_repository: StammdatenRepository,
        studienplan_repository: StudienplanRepository,
        studienfortschritt_repository: StudienfortschrittRepository,
        studienfortschritt_service: StudienfortschrittService,
        noten_service: NotenService,
        abschlussprognose_service: AbschlussPrognoseService,
    ) -> None:
        """
        Initialisiert den Controller mit seinen Abhängigkeiten.

        Args:
            stammdaten_repository:
                Repository zum Laden von Student und Studiengang.
            studienplan_repository:
                Repository zum Laden von Semestern, Modulen und
                Prüfungsleistungen.
            studienfortschritt_repository:
                Repository zum Laden von Modulbelegungen und
                Prüfungsergebnissen.
            studienfortschritt_service:
                Service zur Berechnung des ECTS-Fortschritts und zur
                Gruppierung der Module.
            noten_service:
                Service zur Berechnung des Notendurchschnitts.
            abschlussprognose_service:
                Service zur Berechnung des Zeitfortschritts, der
                Abschlussprognose und des Studienstatus.
        """

        self._stammdaten_repository = stammdaten_repository
        self._studienplan_repository = studienplan_repository
        self._studienfortschritt_repository = (
            studienfortschritt_repository
        )
        self._studienfortschritt_service = studienfortschritt_service
        self._noten_service = noten_service
        self._abschlussprognose_service = abschlussprognose_service

    def lade_dashboard(self) -> DashboardDatenDTO:
        """
        Lädt und berechnet alle für das Dashboard benötigten Daten.

        Returns:
            Ein DashboardDatenDTO mit Kennzahlen und Modulübersichten.

        Raises:
            LookupError:
                Wenn zum Studienmodell keine Semester oder keine Module
                vorhanden sind.
        """

        student = self._stammdaten_repository.lade_student()

        semester = self._studienplan_repository.lade_semester(
            studiengang_id=student.studiengang.id,
            studienmodell=student.studienmodell,
        )

        if not semester:
            raise LookupError(
                "Für den Studiengang und das gewählte Studienmodell "
                "wurden keine Semester gefunden."
            )

        student.studiengang.semester = semester

        alle_module = self._sammle_eindeutige_module(semester)

        if not alle_module:
            raise LookupError(
                "Im geladenen Studienplan wurden keine Module gefunden."
            )

        module_nach_id = {
            modul.id: modul
            for modul in alle_module
        }

        pruefungsleistungen_nach_id = (
            self._erstelle_pruefungsleistungen_nach_id(
                alle_module
            )
        )

        student.modulbelegungen = (
            self._studienfortschritt_repository.lade_modulbelegungen(
                student_id=student.id,
                module_nach_id=module_nach_id,
            )
        )

        student.pruefungsergebnisse = (
            self._studienfortschritt_repository.lade_pruefungsergebnisse(
                student_id=student.id,
                pruefungsleistungen_nach_id=(
                    pruefungsleistungen_nach_id
                ),
            )
        )

        ects_fortschritt = (
            self._studienfortschritt_service.berechne_ects_fortschritt(
                modulbelegungen=student.modulbelegungen,
                gesamt_ects=student.studiengang.gesamt_ects,
            )
        )

        bestandene_module = (
            self._studienfortschritt_service.ermittle_bestandene_module(
                student.modulbelegungen
            )
        )

        erreichte_ects = sum(
            modul.ects
            for modul in bestandene_module
        )

        aktuelle_module = (
            self._studienfortschritt_service.ermittle_aktuelle_module(
                student.modulbelegungen
            )
        )

        offene_module = (
            self._studienfortschritt_service.ermittle_offene_module(
                alle_module=alle_module,
                modulbelegungen=student.modulbelegungen,
            )
        )

        notendurchschnitt = (
            self._noten_service.berechne_notendurchschnitt(
                student.pruefungsergebnisse
            )
        )

        anzahl_semester = len(student.studiengang.semester)

        zeitfortschritt = (
            self._abschlussprognose_service.berechne_zeitfortschritt(
                startdatum=student.startdatum,
                anzahl_semester=anzahl_semester,
            )
        )

        abschlussprognose = (
            self._abschlussprognose_service.prognostiziere_abschlussdatum(
                startdatum=student.startdatum,
                anzahl_semester=anzahl_semester,
                ects_fortschritt=ects_fortschritt,
            )
        )

        studienstatus = (
            self._abschlussprognose_service.ermittle_studienstatus(
                ects_fortschritt=ects_fortschritt,
                zeitfortschritt=zeitfortschritt,
            )
        )

        return DashboardDatenDTO(
            erreichte_ects=erreichte_ects,
            gesamt_ects=student.studiengang.gesamt_ects,
            ects_fortschritt=ects_fortschritt,
            zeitfortschritt=zeitfortschritt,
            notendurchschnitt=notendurchschnitt,
            abschlussprognose=abschlussprognose,
            studienstatus=studienstatus,
            bestandene_module=bestandene_module,
            offene_module=offene_module,
            aktuelle_module=aktuelle_module,
        )

    @staticmethod
    def _sammle_eindeutige_module(
        semester: list[Semester],
    ) -> list[Modul]:
        """
        Sammelt alle Module der Semester ohne doppelte Modul-IDs.

        Die Reihenfolge des ersten Auftretens bleibt erhalten.
        """

        module_nach_id: dict[int, Modul] = {}

        for einzelnes_semester in semester:
            for modul in einzelnes_semester.module:
                module_nach_id.setdefault(
                    modul.id,
                    modul,
                )

        return list(module_nach_id.values())

    @staticmethod
    def _erstelle_pruefungsleistungen_nach_id(
        module: list[Modul],
    ) -> dict[int, Pruefungsleistung]:
        """
        Erstellt ein Nachschlagewerk aller Prüfungsleistungen.

        Returns:
            Dictionary mit der Prüfungsleistungs-ID als Schlüssel.
        """

        pruefungsleistungen_nach_id: dict[
            int,
            Pruefungsleistung,
        ] = {}

        for modul in module:
            for pruefungsleistung in modul.pruefungsleistungen:
                pruefungsleistungen_nach_id.setdefault(
                    pruefungsleistung.id,
                    pruefungsleistung,
                )

        return pruefungsleistungen_nach_id

