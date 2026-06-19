"""
Überprüft die Tabellen und Beziehungen der SQLite-Datenbank.
"""

from pathlib import Path
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATABASE_PATH = PROJECT_ROOT / "dashboard.db"


def pruefe_fremdschluessel(
    connection: sqlite3.Connection,
) -> None:
    """Prüft die referenzielle Integrität der Datenbank."""

    fehler = connection.execute(
        "PRAGMA foreign_key_check"
    ).fetchall()

    print("1. Fremdschlüsselprüfung")

    if fehler:
        for fehlerzeile in fehler:
            print(dict(fehlerzeile))
    else:
        print("Alle Fremdschlüsselbeziehungen sind gültig.")


def zeige_studienplan(
    connection: sqlite3.Connection,
) -> None:
    """Zeigt den Studienplan passend zum Studienmodell des Studenten."""

    datensaetze = connection.execute(
        """
        SELECT
            semester.nummer,
            semester.bezeichnung,
            semester.zeitmodell,
            modul.titel,
            modul.ects
        FROM student
        JOIN studiengang
            ON studiengang.id = student.studiengang_id
        JOIN semester
            ON semester.studiengang_id = studiengang.id
            AND semester.zeitmodell = student.studienmodell
        JOIN semester_modul
            ON semester_modul.semester_id = semester.id
        JOIN modul
            ON modul.id = semester_modul.modul_id
        WHERE student.id = ?
        ORDER BY
            semester.nummer,
            modul.titel
        """,
        (1,),
    ).fetchall()

    print("\n2. Studienplan des Studenten")

    for datensatz in datensaetze:
        print(
            f"{datensatz['bezeichnung']}: "
            f"{datensatz['titel']} "
            f"({datensatz['ects']} ECTS)"
        )


def zeige_modulbelegungen(
    connection: sqlite3.Connection,
) -> None:
    """Zeigt die Modulbelegungen des Studenten."""

    datensaetze = connection.execute(
        """
        SELECT
            modul.titel,
            modulbelegung.status,
            modulbelegung.buchungsdatum,
            modulbelegung.abgeschlossen_am
        FROM modulbelegung
        JOIN modul
            ON modul.id = modulbelegung.modul_id
        WHERE modulbelegung.student_id = ?
        ORDER BY modul.titel
        """,
        (1,),
    ).fetchall()

    print("\n3. Modulbelegungen")

    for datensatz in datensaetze:
        print(
            f"{datensatz['titel']}: "
            f"{datensatz['status']}, "
            f"gebucht am {datensatz['buchungsdatum']}, "
            f"abgeschlossen am "
            f"{datensatz['abgeschlossen_am']}"
        )


def zeige_pruefungsergebnisse(
    connection: sqlite3.Connection,
) -> None:
    """Zeigt die Prüfungsergebnisse des Studenten."""

    datensaetze = connection.execute(
        """
        SELECT
            modul.titel,
            pruefungsleistung.bezeichnung,
            pruefungsleistung.art,
            pruefungsergebnis.status,
            pruefungsergebnis.note,
            pruefungsergebnis.pruefungsdatum
        FROM pruefungsergebnis
        JOIN pruefungsleistung
            ON pruefungsleistung.id =
               pruefungsergebnis.pruefungsleistung_id
        JOIN modul
            ON modul.id = pruefungsleistung.modul_id
        WHERE pruefungsergebnis.student_id = ?
        ORDER BY modul.titel
        """,
        (1,),
    ).fetchall()

    print("\n4. Prüfungsergebnisse")

    for datensatz in datensaetze:
        print(
            f"{datensatz['titel']} – "
            f"{datensatz['bezeichnung']}: "
            f"{datensatz['status']}, "
            f"Note: {datensatz['note']}, "
            f"Datum: {datensatz['pruefungsdatum']}"
        )


def zeige_mehrfachzuordnungen(
    connection: sqlite3.Connection,
) -> None:
    """Zeigt, dass Module verschiedenen Zeitmodellen zugeordnet sein können."""

    datensaetze = connection.execute(
        """
        SELECT
            modul.titel,
            semester.zeitmodell,
            semester.nummer
        FROM semester_modul
        JOIN semester
            ON semester.id = semester_modul.semester_id
        JOIN modul
            ON modul.id = semester_modul.modul_id
        ORDER BY
            modul.titel,
            semester.zeitmodell,
            semester.nummer
        """
    ).fetchall()

    print("\n5. Modulzuordnung zu den Zeitmodellen")

    for datensatz in datensaetze:
        print(
            f"{datensatz['titel']}: "
            f"{datensatz['zeitmodell']}, "
            f"Semester {datensatz['nummer']}"
        )


def main() -> None:
    """Führt alle Datenbankprüfungen aus."""

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.row_factory = sqlite3.Row

        pruefe_fremdschluessel(connection)
        zeige_studienplan(connection)
        zeige_modulbelegungen(connection)
        zeige_pruefungsergebnisse(connection)
        zeige_mehrfachzuordnungen(connection)


if __name__ == "__main__":
    main()
