"""
Programmeinstieg des Studien-Dashboards.
"""

from .application.dashboard_app import DashboardApp


def main() -> None:
    """Startet die Anwendung."""

    app = DashboardApp()
    app.start()


if __name__ == "__main__":
    main()
