"""
Zentrale Verwaltung der SQLite-Datenbankverbindung.

Das Modul stellt allen Repository-Klassen eine einheitlich konfigurierte
Datenbankverbindung zur Verfügung.
"""

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
import sqlite3


# database.py liegt unter src/repositories/.
# parents[2] verweist daher auf das Hauptverzeichnis StudentDashboard.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATABASE_PATH = PROJECT_ROOT / "dashboard.db"


@contextmanager
def datenbankverbindung() -> Iterator[sqlite3.Connection]:
    """
    Öffnet eine konfigurierte Verbindung zur SQLite-Datenbank.

    Die Verbindung verwendet sqlite3.Row, sodass Spalten über ihre Namen
    angesprochen werden können. Fremdschlüsselprüfungen werden für jede
    neue Verbindung aktiviert. Nach der Verwendung wird die Verbindung
    automatisch geschlossen.

    Yields:
        Eine konfigurierte SQLite-Datenbankverbindung.

    Raises:
        FileNotFoundError:
            Wenn die Datenbankdatei dashboard.db nicht vorhanden ist.
    """

    if not DATABASE_PATH.exists():
        raise FileNotFoundError(
            f"Die Datenbank wurde nicht gefunden: {DATABASE_PATH}"
        )

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")

    try:
        yield connection
    finally:
        connection.close()
