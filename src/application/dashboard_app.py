"""
Application-Klasse des Studien-Dashboards.

Die Klasse erzeugt alle benötigten Repository-, Service-, Controller-
und View-Objekte und verbindet die Anwendungsschichten miteinander.
"""

from ..controller.dashboard_controller import DashboardController
from ..repositories.stammdaten_repository import StammdatenRepository
from ..repositories.studienfortschritt_repository import (
    StudienfortschrittRepository,
)
from ..repositories.studienplan_repository import StudienplanRepository
from ..services.abschlussprognose_service import AbschlussPrognoseService
from ..services.noten_service import NotenService
from ..services.studienfortschritt_service import StudienfortschrittService
from ..views.dashboard_view import DashboardView


class DashboardApp:
    """
    Startpunkt und Composition Root des Studien-Dashboards.

    Die Klasse übernimmt ausschließlich die Erzeugung und Verdrahtung
    der Anwendungskomponenten.
    """

    def start(self) -> None:
        """
        Erzeugt alle Anwendungskomponenten und startet das Dashboard.
        """

        stammdaten_repository = StammdatenRepository()
        studienplan_repository = StudienplanRepository()
        studienfortschritt_repository = StudienfortschrittRepository()

        studienfortschritt_service = StudienfortschrittService()
        noten_service = NotenService()
        abschlussprognose_service = AbschlussPrognoseService()

        controller = DashboardController(
            stammdaten_repository=stammdaten_repository,
            studienplan_repository=studienplan_repository,
            studienfortschritt_repository=studienfortschritt_repository,
            studienfortschritt_service=studienfortschritt_service,
            noten_service=noten_service,
            abschlussprognose_service=abschlussprognose_service,
        )

        dashboard_view = DashboardView()

        dashboard_daten = controller.lade_dashboard()

        dashboard_view.zeige_dashboard(dashboard_daten)

