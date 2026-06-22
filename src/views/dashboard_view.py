"""
View-Klasse des Studien-Dashboards.

Die DashboardView ist ausschließlich für die grafische Darstellung
der vom DashboardController bereitgestellten Dashboard-Daten zuständig.
Sie enthält keine fachliche Berechnungs- oder Datenbanklogik.
"""

import tkinter as tk
from tkinter import ttk

from ..dto.dashboard_daten_dto import DashboardDatenDTO


class DashboardView:
    """
    Stellt die Kennzahlen und Modulübersichten des Studien-Dashboards dar.
    """

    HINTERGRUND = "#f5f5f5"
    KARTEN_HINTERGRUND = "#ffffff"
    RAHMENFARBE = "#777777"
    KOPF_HINTERGRUND = "#dddddd"

    def __init__(self) -> None:
        """
        Initialisiert die View.

        Das Hauptfenster wird erst beim Aufruf von zeige_dashboard()
        erzeugt.
        """

        self._fenster: tk.Tk | None = None
        self._hauptbereich: tk.Frame | None = None

    def zeige_dashboard(
        self,
        daten: DashboardDatenDTO,
    ) -> None:
        """
        Erstellt und startet die grafische Benutzeroberfläche.

        Args:
            daten:
                Vom Controller bereitgestellte Dashboard-Daten.
        """

        self._fenster = tk.Tk()
        self._fenster.title("Studien-Dashboard")
        self._fenster.geometry("1120x980")
        self._fenster.minsize(950, 800)
        self._fenster.configure(bg=self.HINTERGRUND)

        self._konfiguriere_stile()

        self._hauptbereich = tk.Frame(
            self._fenster,
            bg=self.HINTERGRUND,
        )
        self._hauptbereich.pack(
            fill=tk.BOTH,
            expand=True,
            padx=25,
            pady=18,
        )

        self._erstelle_kopfbereich()
        self._erstelle_ects_bereich(daten)
        self._erstelle_kennzahlenbereich(daten)
        self._erstelle_aktuelle_kurse(daten)
        self._erstelle_abschlussbereich(daten)

        self._fenster.mainloop()

    def _konfiguriere_stile(self) -> None:
        """
        Konfiguriert die Darstellung des Fortschrittsbalkens.
        """

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Dashboard.Horizontal.TProgressbar",
            troughcolor="#eeeeee",
            background="#aaaaaa",
            bordercolor="#777777",
            lightcolor="#aaaaaa",
            darkcolor="#aaaaaa",
            thickness=35,
        )

    def _erstelle_kopfbereich(self) -> None:
        """
        Erstellt den Titelbereich des Dashboards.
        """

        if self._hauptbereich is None:
            return

        kopfbereich = tk.Frame(
            self._hauptbereich,
            bg=self.KOPF_HINTERGRUND,
            highlightbackground=self.RAHMENFARBE,
            highlightthickness=1,
            height=95,
        )
        kopfbereich.pack(
            fill=tk.X,
            pady=(0, 12),
        )
        kopfbereich.pack_propagate(False)

        titel = tk.Label(
            kopfbereich,
            text="Studien-Dashboard",
            bg=self.KOPF_HINTERGRUND,
            font=("Segoe UI", 24, "bold"),
        )
        titel.pack(
            expand=True,
        )

    def _erstelle_ects_bereich(
        self,
        daten: DashboardDatenDTO,
    ) -> None:
        """
        Erstellt den Bereich für den ECTS-Fortschritt.
        """

        if self._hauptbereich is None:
            return

        bereich = tk.Frame(
            self._hauptbereich,
            bg=self.KARTEN_HINTERGRUND,
            highlightbackground=self.RAHMENFARBE,
            highlightthickness=1,
        )
        bereich.pack(
            fill=tk.X,
            padx=45,
            pady=(0, 16),
        )

        inhalt = tk.Frame(
            bereich,
            bg=self.KARTEN_HINTERGRUND,
        )
        inhalt.pack(
            fill=tk.X,
            padx=35,
            pady=28,
        )

        titel = tk.Label(
            inhalt,
            text="ECTS-Fortschritt",
            bg=self.KARTEN_HINTERGRUND,
            font=("Segoe UI", 15, "bold"),
            anchor="w",
        )
        titel.pack(
            fill=tk.X,
            pady=(0, 15),
        )

        beschreibung = tk.Label(
            inhalt,
            text=(
                f"{daten.erreichte_ects} / "
                f"{daten.gesamt_ects} ECTS erreicht"
            ),
            bg=self.KARTEN_HINTERGRUND,
            font=("Segoe UI", 12),
            anchor="w",
        )
        beschreibung.pack(
            fill=tk.X,
            pady=(0, 15),
        )

        fortschrittszeile = tk.Frame(
            inhalt,
            bg=self.KARTEN_HINTERGRUND,
        )
        fortschrittszeile.pack(
            fill=tk.X,
        )

        fortschrittsbalken = ttk.Progressbar(
            fortschrittszeile,
            orient=tk.HORIZONTAL,
            mode="determinate",
            maximum=100,
            value=daten.ects_fortschritt,
            style="Dashboard.Horizontal.TProgressbar",
        )
        fortschrittsbalken.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
        )

        prozent_label = tk.Label(
            fortschrittszeile,
            text=f"{daten.ects_fortschritt:.0f} %",
            bg=self.KARTEN_HINTERGRUND,
            font=("Segoe UI", 11),
            width=8,
            anchor="e",
        )
        prozent_label.pack(
            side=tk.RIGHT,
            padx=(20, 0),
        )

    def _erstelle_kennzahlenbereich(
        self,
        daten: DashboardDatenDTO,
    ) -> None:
        """
        Erstellt die drei kompakten Kennzahlenkarten.
        """

        if self._hauptbereich is None:
            return

        aussenrahmen = tk.Frame(
            self._hauptbereich,
            bg=self.HINTERGRUND,
        )
        aussenrahmen.pack(
            fill=tk.X,
            pady=(0, 16),
        )

        kennzahlenbereich = tk.Frame(
            aussenrahmen,
            bg=self.HINTERGRUND,
        )
        kennzahlenbereich.pack()

        notendurchschnitt = (
            f"{daten.notendurchschnitt:.2f}"
            if daten.notendurchschnitt > 0
            else "–"
        )

        self._erstelle_kennzahlkarte(
            parent=kennzahlenbereich,
            titel="Notendurchschnitt",
            wert=notendurchschnitt,
        )

        self._erstelle_kennzahlkarte(
            parent=kennzahlenbereich,
            titel="Bestandene Module",
            wert=str(len(daten.bestandene_module)),
        )

        self._erstelle_kennzahlkarte(
            parent=kennzahlenbereich,
            titel="Offene Module",
            wert=str(len(daten.offene_module)),
        )

    def _erstelle_kennzahlkarte(
        self,
        parent: tk.Frame,
        titel: str,
        wert: str,
    ) -> None:
        """
        Erstellt eine einzelne kompakte Kennzahlenkarte.

        Args:
            parent:
                Übergeordneter Tkinter-Frame.
            titel:
                Bezeichnung der Kennzahl.
            wert:
                Darzustellender Kennzahlenwert.
        """

        karte = tk.Frame(
            parent,
            bg=self.KARTEN_HINTERGRUND,
            highlightbackground=self.RAHMENFARBE,
            highlightthickness=1,
            width=235,
            height=105,
        )
        karte.pack(
            side=tk.LEFT,
            padx=10,
        )
        karte.pack_propagate(False)

        titel_label = tk.Label(
            karte,
            text=titel,
            bg=self.KARTEN_HINTERGRUND,
            font=("Segoe UI", 10, "bold"),
        )
        titel_label.pack(
            pady=(22, 4),
        )

        wert_label = tk.Label(
            karte,
            text=wert,
            bg=self.KARTEN_HINTERGRUND,
            font=("Segoe UI", 18),
        )
        wert_label.pack()

    def _erstelle_aktuelle_kurse(
        self,
        daten: DashboardDatenDTO,
    ) -> None:
        """
        Erstellt die Liste der aktuell gebuchten Kurse.
        """

        if self._hauptbereich is None:
            return

        bereich = tk.Frame(
            self._hauptbereich,
            bg=self.KARTEN_HINTERGRUND,
            highlightbackground=self.RAHMENFARBE,
            highlightthickness=1,
        )
        bereich.pack(
            fill=tk.BOTH,
            expand=True,
            padx=45,
            pady=(0, 16),
        )

        titel = tk.Label(
            bereich,
            text="Aktuell gebuchte Kurse",
            bg=self.KARTEN_HINTERGRUND,
            font=("Segoe UI", 15, "bold"),
            anchor="w",
        )
        titel.pack(
            fill=tk.X,
            padx=35,
            pady=(25, 12),
        )

        listenbereich = tk.Frame(
            bereich,
            bg=self.KARTEN_HINTERGRUND,
        )
        listenbereich.pack(
            fill=tk.BOTH,
            expand=True,
            padx=35,
            pady=(0, 25),
        )

        scrollbar = tk.Scrollbar(
            listenbereich,
            orient=tk.VERTICAL,
        )
        scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y,
        )

        kursliste = tk.Text(
            listenbereich,
            height=6,
            wrap=tk.WORD,
            font=("Segoe UI", 10),
            bg=self.KARTEN_HINTERGRUND,
            relief=tk.FLAT,
            borderwidth=0,
            padx=0,
            pady=0,
            yscrollcommand=scrollbar.set,
        )
        kursliste.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
        )

        scrollbar.config(
            command=kursliste.yview,
        )

        if daten.aktuelle_module:
            for modul in daten.aktuelle_module:
                kursliste.insert(
                    tk.END,
                    f"• {modul.titel} ({modul.ects} ECTS)\n",
                )
        else:
            kursliste.insert(
                tk.END,
                "Derzeit sind keine Kurse gebucht.",
            )

        kursliste.config(
            state=tk.DISABLED,
        )

    def _erstelle_abschlussbereich(
        self,
        daten: DashboardDatenDTO,
    ) -> None:
        """
        Erstellt den Bereich für die Abschlussprognose.
        """

        if self._hauptbereich is None:
            return

        bereich = tk.Frame(
            self._hauptbereich,
            bg=self.KARTEN_HINTERGRUND,
            highlightbackground=self.RAHMENFARBE,
            highlightthickness=1,
        )
        bereich.pack(
            fill=tk.X,
            padx=45,
            pady=(0, 5),
        )

        inhalt = tk.Frame(
            bereich,
            bg=self.KARTEN_HINTERGRUND,
        )
        inhalt.pack(
            fill=tk.X,
            padx=35,
            pady=28,
        )

        titel = tk.Label(
            inhalt,
            text="Geplanter Studienabschluss",
            bg=self.KARTEN_HINTERGRUND,
            font=("Segoe UI", 15, "bold"),
            anchor="w",
        )
        titel.pack(
            fill=tk.X,
            pady=(0, 16),
        )

        prognose_label = tk.Label(
            inhalt,
            text=(
                "Prognostizierter Abschluss: "
                f"{daten.abschlussprognose:%d.%m.%Y}"
            ),
            bg=self.KARTEN_HINTERGRUND,
            font=("Segoe UI", 11),
            anchor="w",
        )
        prognose_label.pack(
            fill=tk.X,
            pady=(0, 10),
        )

        status_label = tk.Label(
            inhalt,
            text=f"Status: {daten.studienstatus}",
            bg=self.KARTEN_HINTERGRUND,
            font=("Segoe UI", 11),
            anchor="w",
        )
        status_label.pack(
            fill=tk.X,
            pady=(0, 10),
        )

        zeitfortschritt_label = tk.Label(
            inhalt,
            text=(
                f"Zeitfortschritt: "
                f"{daten.zeitfortschritt:.1f} %"
            ),
            bg=self.KARTEN_HINTERGRUND,
            font=("Segoe UI", 10),
            anchor="w",
        )
        zeitfortschritt_label.pack(
            fill=tk.X,
        )