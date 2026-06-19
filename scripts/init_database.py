"""
Erstellt die SQLite-Datenbank des Studien-Dashboards.

Das Skript legt alle Tabellen, Fremdschlüssel und Testdaten neu an.
Es ist ausschließlich für die Entwicklungs- und Testphase vorgesehen.
"""

from pathlib import Path
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATABASE_PATH = PROJECT_ROOT / "dashboard.db"


def erstelle_tabellen(connection: sqlite3.Connection) -> None:
    """Entfernt vorhandene Tabellen und erstellt das Datenbankschema neu."""

    connection.executescript(
        """
        DROP TABLE IF EXISTS pruefungsergebnis;
        DROP TABLE IF EXISTS modulbelegung;
        DROP TABLE IF EXISTS pruefungsleistung;
        DROP TABLE IF EXISTS semester_modul;
        DROP TABLE IF EXISTS modul;
        DROP TABLE IF EXISTS semester;
        DROP TABLE IF EXISTS student;
        DROP TABLE IF EXISTS studiengang;

        CREATE TABLE studiengang (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            abschluss TEXT NOT NULL
                CHECK (abschluss IN ('Bachelor', 'Master')),
            gesamt_ects INTEGER NOT NULL
                CHECK (gesamt_ects > 0)
        );

        CREATE TABLE student (
            id INTEGER PRIMARY KEY,
            matrikelnummer TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            startdatum TEXT NOT NULL,
            studienmodell TEXT NOT NULL
                CHECK (
                    studienmodell IN (
                        'Vollzeit',
                        'Teilzeit I',
                        'Teilzeit II'
                    )
                ),
            studiengang_id INTEGER NOT NULL,
            FOREIGN KEY (studiengang_id)
                REFERENCES studiengang(id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );

        CREATE TABLE semester (
            id INTEGER PRIMARY KEY,
            studiengang_id INTEGER NOT NULL,
            nummer INTEGER NOT NULL
                CHECK (nummer > 0),
            bezeichnung TEXT NOT NULL,
            zeitmodell TEXT NOT NULL
                CHECK (
                    zeitmodell IN (
                        'Vollzeit',
                        'Teilzeit I',
                        'Teilzeit II'
                    )
                ),
            UNIQUE (studiengang_id, zeitmodell, nummer),
            FOREIGN KEY (studiengang_id)
                REFERENCES studiengang(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        );

        CREATE TABLE modul (
            id INTEGER PRIMARY KEY,
            titel TEXT NOT NULL UNIQUE,
            ects INTEGER NOT NULL
                CHECK (ects > 0)
        );

        CREATE TABLE semester_modul (
            semester_id INTEGER NOT NULL,
            modul_id INTEGER NOT NULL,
            PRIMARY KEY (semester_id, modul_id),
            FOREIGN KEY (semester_id)
                REFERENCES semester(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
            FOREIGN KEY (modul_id)
                REFERENCES modul(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        );

        CREATE TABLE pruefungsleistung (
            id INTEGER PRIMARY KEY,
            modul_id INTEGER NOT NULL,
            art TEXT NOT NULL
                CHECK (
                    art IN (
                        'Klausur',
                        'Workbook',
                        'Portfolio',
                        'Projekt',
                        'Fachpräsentation'
                    )
                ),
            bezeichnung TEXT NOT NULL,
            UNIQUE (modul_id, bezeichnung),
            FOREIGN KEY (modul_id)
                REFERENCES modul(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        );

        CREATE TABLE modulbelegung (
            id INTEGER PRIMARY KEY,
            student_id INTEGER NOT NULL,
            modul_id INTEGER NOT NULL,
            status TEXT NOT NULL
                CHECK (
                    status IN (
                        'Gebucht',
                        'Abgeschlossen'
                    )
                ),
            buchungsdatum TEXT NOT NULL,
            abgeschlossen_am TEXT,
            UNIQUE (student_id, modul_id),
            CHECK (
                abgeschlossen_am IS NULL
                OR abgeschlossen_am >= buchungsdatum
            ),
            CHECK (
                (
                    status = 'Gebucht'
                    AND abgeschlossen_am IS NULL
                )
                OR
                (
                    status = 'Abgeschlossen'
                    AND abgeschlossen_am IS NOT NULL
                )
            ),
            FOREIGN KEY (student_id)
                REFERENCES student(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
            FOREIGN KEY (modul_id)
                REFERENCES modul(id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );

CREATE TABLE pruefungsergebnis (
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    pruefungsleistung_id INTEGER NOT NULL,

    status TEXT NOT NULL
        CHECK (
            status IN (
                'Offen',
                'Bestanden',
                'Nicht bestanden'
            )
        ),

    note REAL,
    pruefungsdatum TEXT,

    UNIQUE (student_id, pruefungsleistung_id),

    CHECK (
        note IS NULL
        OR note IN (
            1.0, 1.3, 1.7,
            2.0, 2.3, 2.7,
            3.0, 3.3, 3.7,
            4.0, 4.3, 4.7,
            5.0
        )
    ),

    CHECK (
        (
            status = 'Offen'
            AND note IS NULL
            AND pruefungsdatum IS NULL
        )
        OR
        (
            status = 'Bestanden'
            AND note IN (
                1.0, 1.3, 1.7,
                2.0, 2.3, 2.7,
                3.0, 3.3, 3.7,
                4.0, 4.3, 4.7
            )
            AND pruefungsdatum IS NOT NULL
        )
        OR
        (
            status = 'Nicht bestanden'
            AND note = 5.0
            AND pruefungsdatum IS NOT NULL
        )
    ),

    FOREIGN KEY (student_id)
        REFERENCES student(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    FOREIGN KEY (pruefungsleistung_id)
        REFERENCES pruefungsleistung(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);   """
    )


def fuege_testdaten_ein(connection: sqlite3.Connection) -> None:
    """Fügt zusammenhängende Testdaten für alle Tabellen ein."""

    connection.execute(
        """
        INSERT INTO studiengang (
            id,
            name,
            abschluss,
            gesamt_ects
        )
        VALUES (?, ?, ?, ?)
        """,
        (1, "Softwareentwicklung", "Bachelor", 180),
    )

    connection.execute(
        """
        INSERT INTO student (
            id,
            matrikelnummer,
            name,
            startdatum,
            studienmodell,
            studiengang_id
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            1,
            "12345678",
            "Teststudentin",
            "2025-10-01",
            "Vollzeit",
            1,
        ),
    )

    semester = [
        (1, 1, 1, "1. Semester", "Vollzeit"),
        (2, 1, 2, "2. Semester", "Vollzeit"),
        (3, 1, 1, "1. Semester", "Teilzeit I"),
        (4, 1, 2, "2. Semester", "Teilzeit I"),
        (5, 1, 3, "3. Semester", "Teilzeit I"),
        (6, 1, 4, "4. Semester", "Teilzeit I"),
    ]

    connection.executemany(
        """
        INSERT INTO semester (
            id,
            studiengang_id,
            nummer,
            bezeichnung,
            zeitmodell
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        semester,
    )

    module = [
        (
            1,
            "Objektorientierte und funktionale Programmierung mit Python",
            5,
        ),
        (2, "Datenbanken", 5),
        (3, "Softwarearchitektur", 5),
        (4, "Mathematik", 5),
        (5, "Projektmanagement", 5),
    ]

    connection.executemany(
        """
        INSERT INTO modul (
            id,
            titel,
            ects
        )
        VALUES (?, ?, ?)
        """,
        module,
    )

    semester_module = [
        # Vollzeit
        (1, 1),
        (1, 2),
        (1, 4),
        (2, 3),
        (2, 5),

        # Teilzeit I
        (3, 1),
        (3, 4),
        (4, 2),
        (5, 3),
        (6, 5),
    ]

    connection.executemany(
        """
        INSERT INTO semester_modul (
            semester_id,
            modul_id
        )
        VALUES (?, ?)
        """,
        semester_module,
    )

    pruefungsleistungen = [
        (1, 1, "Portfolio", "Studien-Dashboard"),
        (2, 2, "Klausur", "Datenbankgrundlagen"),
        (3, 3, "Projekt", "Architekturentwurf"),
        (4, 4, "Klausur", "Mathematikprüfung"),
        (5, 5, "Workbook", "Projektplanung"),
    ]

    connection.executemany(
        """
        INSERT INTO pruefungsleistung (
            id,
            modul_id,
            art,
            bezeichnung
        )
        VALUES (?, ?, ?, ?)
        """,
        pruefungsleistungen,
    )

    modulbelegungen = [
        (
            1,
            1,
            1,
            "Abgeschlossen",
            "2026-04-01",
            "2026-06-15",
        ),
        (
            2,
            1,
            2,
            "Gebucht",
            "2026-06-01",
            None,
        ),
        (
            3,
            1,
            4,
            "Abgeschlossen",
            "2025-10-01",
            "2026-02-20",
        ),
    ]

    connection.executemany(
        """
        INSERT INTO modulbelegung (
            id,
            student_id,
            modul_id,
            status,
            buchungsdatum,
            abgeschlossen_am
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        modulbelegungen,
    )

    pruefungsergebnisse = [
        (
            1,
            1,
            1,
            "Bestanden",
            1.7,
            "2026-06-15",
        ),
        (
            2,
            1,
            2,
            "Offen",
            None,
            None,
        ),
        (
            3,
            1,
            4,
            "Bestanden",
            2.3,
            "2026-02-20",
        ),
    ]

    connection.executemany(
        """
        INSERT INTO pruefungsergebnis (
            id,
            student_id,
            pruefungsleistung_id,
            status,
            note,
            pruefungsdatum
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        pruefungsergebnisse,
    )


def main() -> None:
    """Erstellt die Datenbank und fügt die Testdaten ein."""

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")

        erstelle_tabellen(connection)
        fuege_testdaten_ein(connection)

    print(f"Datenbank wurde erstellt: {DATABASE_PATH}")


if __name__ == "__main__":
    main()
