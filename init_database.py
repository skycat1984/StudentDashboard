"""
Erstellt die SQLite-Datenbank des Studien-Dashboards.

Das Skript legt das vollständige Datenbankschema neu an und übernimmt den
Studienablaufplan des B.Sc. Softwareentwicklung für die Studienmodelle
Vollzeit, Teilzeit I und Teilzeit II. Zusätzlich werden zusammenhängende
Testdaten für eine Teststudentin eingefügt.

Hinweis:
    Das Skript ist für die Entwicklungs- und Testphase vorgesehen. Beim
    Ausführen wird eine vorhandene dashboard.db vollständig neu erstellt.
"""

from pathlib import Path
import sqlite3

# init_database.py liegt direkt im Hauptverzeichnis.
PROJECT_ROOT = Path(__file__).resolve().parent
DATABASE_PATH = PROJECT_ROOT / "dashboard.db"

STUDIENGANG_ID = 1
STUDENT_ID = 1
TEST_STUDIENMODELL = "Teilzeit II"


MODULE: list[tuple[int, str, int]] = [
    (1, "Grundlagen der industriellen Softwaretechnik", 5),
    (2, "Einführung in das wissenschaftliche Arbeiten für IT und Technik", 5),
    (3, "Requirements Engineering", 5),
    (4, "Spezifikation", 5),
    (5, "Grundlagen der objektorientierten Programmierung mit Java", 5),
    (6, "Datenmodellierung und Datenbanksysteme", 5),
    (7, "Datenstruktur und Java-Klassenbibliothek", 5),
    (8, "Kollaboratives Arbeiten", 5),
    (9, "Programmierung von Web-Anwendungsoberflächen", 5),
    (10, "Algorithmen, Datenstrukturen und Programmiersprachen", 5),
    (11, "Qualitätssicherung im Softwareprozess", 5),
    (12, "IT-Architekturmanagement", 5),
    (
        13,
        "Programmierung von industriellen Informationssystemen mit Java EE",
        5,
    ),
    (14, "Ethik und Nachhaltigkeit in der IT", 5),
    (15, "IT-Projektmanagement", 5),
    (16, "Techniken und Methoden der agilen Softwareentwicklung", 5),
    (
        17,
        "Mobile Software Engineering am Beispiel der Android-Plattform",
        5,
    ),
    (18, 'Seminar "Software Engineering"', 5),
    (19, "Projekt Agiles Software Engineering", 5),
    (20, "IT-Infrastruktur", 5),
    (21, "IT-Service Management", 5),
    (22, "Projekt: Mobile Software Engineering II", 5),
    (23, "Cloud Programming", 5),
    (24, "Einführung in Datenschutz und IT-Sicherheit", 5),
    (25, "DevOps und Continuous Delivery", 5),
    (26, "Gestaltung und Ergonomie von User Interfaces", 5),
    (27, "Einführung in die Programmierung mit Python", 5),
    (28, "Projekt: Software Development", 5),
    (
        29,
        "Data Science und objektorientierte Programmierung mit Python",
        10,
    ),
    (30, "Internet of Things und Embedded Systems", 10),
    (31, "Augmented, Mixed und Virtual Reality", 10),
    (32, "Bachelorarbeit und Kolloquium", 10),
]


SEMESTERPLAN: dict[str, list[list[int]]] = {
    "Vollzeit": [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29],
        [30, 31, 32],
    ],
    "Teilzeit I": [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18],
        [19, 20, 21, 22, 23],
        [24, 25, 26, 27],
        [28, 29, 30],
        [31, 32],
    ],
    "Teilzeit II": [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18],
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27],
        [28, 29],
        [30, 31],
        [32],
    ],
}


PRUEFUNGSLEISTUNGEN: list[tuple[int, int, str, str]] = [
    (1, 1, "Klausur", "Klausur"),
    (2, 2, "Workbook", "Advanced Workbook"),
    (3, 3, "Klausur", "Klausur"),
    (4, 4, "Klausur", "Klausur"),
    (5, 5, "Klausur", "Klausur"),
    (6, 6, "Klausur", "Klausur"),
    (7, 7, "Klausur", "Klausur"),
    (8, 8, "Fachpräsentation", "Fachpräsentation"),
    (9, 9, "Projekt", "Fallstudie"),
    (10, 10, "Klausur", "Klausur"),
    (11, 11, "Klausur", "Klausur"),
    (12, 12, "Klausur", "Klausur"),
    (13, 13, "Projekt", "Fallstudie"),
    (14, 14, "Projekt", "Fallstudie"),
    (15, 15, "Klausur", "Klausur"),
    (16, 16, "Klausur", "Klausur"),
    (17, 17, "Klausur", "Klausur"),
    (18, 18, "Projekt", "Seminararbeit"),
    (19, 19, "Projekt", "Projektbericht"),
    (20, 20, "Klausur", "Klausur"),
    (21, 21, "Workbook", "Advanced Workbook"),
    (22, 22, "Projekt", "Projektbericht"),
    (23, 23, "Portfolio", "Portfolio"),
    (24, 24, "Klausur", "Klausur"),
    (25, 25, "Projekt", "Fallstudie"),
    (26, 26, "Klausur", "Klausur"),
    (27, 27, "Klausur", "Klausur"),
    (28, 28, "Fachpräsentation", "Projektpräsentation"),
    (29, 29, "Projekt", "Modulprüfung"),
    (30, 30, "Projekt", "Modulprüfung"),
    (31, 31, "Projekt", "Modulprüfung"),
    (32, 32, "Projekt", "Bachelorarbeit"),
    (33, 32, "Fachpräsentation", "Kolloquium"),
]


ABGESCHLOSSENE_MODULE: list[
    tuple[int, str, str, float]
] = [
    (1, "2023-10-01", "2023-11-15", 1.7),
    (2, "2023-10-01", "2023-12-15", 1.3),
    (3, "2023-11-01", "2024-01-31", 2.0),
    (4, "2024-01-01", "2024-03-15", 1.7),
    (5, "2024-02-01", "2024-04-30", 2.3),
    (6, "2024-03-01", "2024-06-15", 1.7),
    (7, "2024-05-01", "2024-07-31", 2.0),
    (8, "2024-06-01", "2024-08-31", 1.3),
    (9, "2024-07-01", "2024-10-15", 1.7),
    (10, "2024-09-01", "2024-11-30", 2.0),
    (11, "2024-10-01", "2025-01-15", 1.3),
    (12, "2024-11-01", "2025-02-28", 2.3),
    (13, "2025-01-01", "2025-03-31", 1.7),
    (14, "2025-02-01", "2025-04-30", 1.3),
    (15, "2025-03-01", "2025-06-30", 2.0),
    (16, "2025-05-01", "2025-08-31", 1.7),
    (17, "2025-06-01", "2025-10-31", 1.3),
    (18, "2025-08-01", "2025-12-15", 1.7),
]


AKTUELLE_MODULE: list[tuple[int, str]] = [
    (23, "2026-05-01"),
    (27, "2026-05-15"),
    (28, "2026-06-01"),
]


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
                    AND note BETWEEN 1.0 AND 4.7
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
                ON DELETE CASCADE,
            FOREIGN KEY (pruefungsleistung_id)
                REFERENCES pruefungsleistung(id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );
        """
    )


def fuege_stammdaten_ein(connection: sqlite3.Connection) -> None:
    """Fügt Studiengang und Teststudentin ein."""

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
        (
            STUDIENGANG_ID,
            "Softwareentwicklung",
            "Bachelor",
            180,
        ),
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
            STUDENT_ID,
            "12345678",
            "Teststudentin",
            "2023-10-01",
            TEST_STUDIENMODELL,
            STUDIENGANG_ID,
        ),
    )


def fuege_semester_ein(
    connection: sqlite3.Connection,
) -> dict[tuple[str, int], int]:
    """Fügt alle Semester der drei Studienmodelle ein."""

    semester_datensaetze: list[tuple[int, int, int, str, str]] = []
    semester_ids: dict[tuple[str, int], int] = {}
    naechste_id = 1

    for zeitmodell, semesterlisten in SEMESTERPLAN.items():
        for nummer in range(1, len(semesterlisten) + 1):
            semester_ids[(zeitmodell, nummer)] = naechste_id
            semester_datensaetze.append(
                (
                    naechste_id,
                    STUDIENGANG_ID,
                    nummer,
                    f"{nummer}. Semester",
                    zeitmodell,
                )
            )
            naechste_id += 1

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
        semester_datensaetze,
    )

    return semester_ids


def fuege_module_ein(connection: sqlite3.Connection) -> None:
    """Fügt alle Pflicht- und ausgewählten Wahlpflichtmodule ein."""

    connection.executemany(
        """
        INSERT INTO modul (
            id,
            titel,
            ects
        )
        VALUES (?, ?, ?)
        """,
        MODULE,
    )


def fuege_semesterzuordnungen_ein(
    connection: sqlite3.Connection,
    semester_ids: dict[tuple[str, int], int],
) -> None:
    """Ordnet die Module den Semestern aller Studienmodelle zu."""

    semester_module: list[tuple[int, int]] = []

    for zeitmodell, semesterlisten in SEMESTERPLAN.items():
        for nummer, modul_ids in enumerate(semesterlisten, start=1):
            semester_id = semester_ids[(zeitmodell, nummer)]

            for modul_id in modul_ids:
                semester_module.append((semester_id, modul_id))

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


def fuege_pruefungsleistungen_ein(
    connection: sqlite3.Connection,
) -> None:
    """Fügt die Prüfungsleistungen der Module ein."""

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
        PRUEFUNGSLEISTUNGEN,
    )


def fuege_testfortschritt_ein(
    connection: sqlite3.Connection,
) -> None:
    """Fügt abgeschlossene und aktuell gebuchte Testmodule ein."""

    modulbelegungen: list[
        tuple[int, int, int, str, str, str | None]
    ] = []
    pruefungsergebnisse: list[
        tuple[int, int, int, str, float | None, str | None]
    ] = []

    naechste_belegung_id = 1
    naechstes_ergebnis_id = 1

    for modul_id, buchungsdatum, abgeschlossen_am, note in (
        ABGESCHLOSSENE_MODULE
    ):
        modulbelegungen.append(
            (
                naechste_belegung_id,
                STUDENT_ID,
                modul_id,
                "Abgeschlossen",
                buchungsdatum,
                abgeschlossen_am,
            )
        )
        pruefungsergebnisse.append(
            (
                naechstes_ergebnis_id,
                STUDENT_ID,
                modul_id,
                "Bestanden",
                note,
                abgeschlossen_am,
            )
        )
        naechste_belegung_id += 1
        naechstes_ergebnis_id += 1

    for modul_id, buchungsdatum in AKTUELLE_MODULE:
        modulbelegungen.append(
            (
                naechste_belegung_id,
                STUDENT_ID,
                modul_id,
                "Gebucht",
                buchungsdatum,
                None,
            )
        )
        pruefungsergebnisse.append(
            (
                naechstes_ergebnis_id,
                STUDENT_ID,
                modul_id,
                "Offen",
                None,
                None,
            )
        )
        naechste_belegung_id += 1
        naechstes_ergebnis_id += 1

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


def validiere_studienplan() -> None:
    """Prüft Semesteranzahl und ECTS-Summe aller Studienmodelle."""

    ects_nach_modul_id = {
        modul_id: ects
        for modul_id, _, ects in MODULE
    }

    erwartete_semesteranzahl = {
        "Vollzeit": 6,
        "Teilzeit I": 8,
        "Teilzeit II": 12,
    }

    for zeitmodell, semesterlisten in SEMESTERPLAN.items():
        if len(semesterlisten) != erwartete_semesteranzahl[zeitmodell]:
            raise ValueError(
                f"Ungültige Semesteranzahl für {zeitmodell}."
            )

        modul_ids = [
            modul_id
            for semester in semesterlisten
            for modul_id in semester
        ]

        if len(modul_ids) != len(set(modul_ids)):
            raise ValueError(
                f"Ein Modul ist in {zeitmodell} mehrfach zugeordnet."
            )

        gesamt_ects = sum(
            ects_nach_modul_id[modul_id]
            for modul_id in modul_ids
        )

        if gesamt_ects != 180:
            raise ValueError(
                f"{zeitmodell} enthält {gesamt_ects} statt 180 ECTS."
            )


def main() -> None:
    """Erstellt die Datenbank und fügt Studienplan und Testdaten ein."""

    validiere_studienplan()

    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")

        erstelle_tabellen(connection)
        fuege_stammdaten_ein(connection)
        semester_ids = fuege_semester_ein(connection)
        fuege_module_ein(connection)
        fuege_semesterzuordnungen_ein(
            connection,
            semester_ids,
        )
        fuege_pruefungsleistungen_ein(connection)
        fuege_testfortschritt_ein(connection)

    erreichte_ects = sum(
        next(
            ects
            for gespeicherte_id, _, ects in MODULE
            if gespeicherte_id == modul_id
        )
        for modul_id, _, _, _ in ABGESCHLOSSENE_MODULE
    )

    offene_module = (
        len(MODULE)
        - len(ABGESCHLOSSENE_MODULE)
        - len(AKTUELLE_MODULE)
    )

    print(f"Datenbank wurde erstellt: {DATABASE_PATH}")
    print("Studienplan: Vollzeit, Teilzeit I und Teilzeit II")
    print(f"Teststudienmodell: {TEST_STUDIENMODELL}")
    print(
        "Testfortschritt: "
        f"{len(ABGESCHLOSSENE_MODULE)} abgeschlossene Module "
        f"({erreichte_ects} ECTS), "
        f"{len(AKTUELLE_MODULE)} aktuelle Module, "
        f"{offene_module} offene Module"
    )


if __name__ == "__main__":
    main()
