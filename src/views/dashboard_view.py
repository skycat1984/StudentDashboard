"""
Tkinter-View zur Darstellung des Studien-Dashboards.

Die View erhält ausschließlich bereits aufbereitete Daten über das
DashboardDatenDTO. Sie enthält keine Datenbankzugriffe und keine
fachlichen Berechnungen.
"""

import tkinter as tk
from tkinter import ttk

from ..dto.dashboard_daten_dto import DashboardDatenDTO


class DashboardView:
    """Stellt das Studien-Dashboard mit Tkinter dar."""

    def __init__(self) -> None:
        """Erzeugt und konfiguriert das Hauptfenster."""

        self._fenster = tk.Tk()
        self._fenster.title("Studien-Dashboard")
        self._fenster.geometry("900x780")
        self._fenster.minsize(760, 680)
        self._fenster.configure(bg="#f5f5f5")

        self._konfiguriere_stile()

        self._hauptbereich = tk.Frame(
            self._fenster,
            bg="#f5f5f5",
            padx=20,
            pady=15,
        )
        self._hauptbereich.pack(
            fill=tk.BOTH,
            expand=True,
        )

    def zeige_dashboard(self, daten: DashboardDatenDTO) -> None:
        """
        Zeigt die aufbereiteten Dashboard-Daten an.

        Args:
            daten:
                Kennzahlen und Modullisten für das Dashboard.
        """

        self._leere_hauptbereich()

        self._erstelle_kopfbereich()
        self._erstelle_ects_bereich(daten)
        self._erstelle_kennzahlenbereich(daten)
        self._erstelle_aktuelle_module(daten)
        self._erstelle_abschlussbereich(daten)

        self._fenster.mainloop()

    def _erstelle_kopfbereich(self) -> None:
        """Erstellt die Überschrift des Dashboards."""

        kopfbereich = tk.Frame(
            self._hauptbereich,
            bg="#d9d9d9",
            highlightbackground="#888888",
            highlightthickness=1,
            height=75,
        )
        kopfbereich.pack(
            fill=tk.X,
            pady=(0, 10),
        )
        kopfbereich.pack_propagate(False)

        titel = tk.Label(
            kopfbereich,
            text="Studien-Dashboard",
            bg="#d9d9d9",
            font=("Segoe UI", 20, "bold"),
        )
        titel.pack(expand=True)

    def _erstelle_ects_bereich(
        self,
        daten: DashboardDatenDTO,
    ) -> None:
        """Erstellt den ECTS-Fortschrittsbereich."""

        bereich = self._erstelle_abschnitt(
            titel="ECTS-Fortschritt",
        )

        fortschritt_text = tk.Label(
    bereich,
    text=(
        f"{daten.erreichte_ects} / "
        f"{daten.gesamt_ects} ECTS erreicht"
    ),
    bg="#f7f7f7",
    font=("Segoe UI", 11),
    anchor="w",
)
        fortschritt_text.pack(
            fill=tk.X,
            padx=28,
            pady=(0, 10),
        )

        balkenbereich = tk.Frame(
            bereich,
            bg="#f7f7f7",
        )
        balkenbereich.pack(
            fill=tk.X,
            padx=28,
            pady=(0, 15),
        )

        fortschrittsbalken = ttk.Progressbar(
            balkenbereich,
            maximum=100,
            value=self._begrenze_prozentwert(
                daten.ects_fortschritt
            ),
            style="Dashboard.Horizontal.TProgressbar",
        )
        fortschrittsbalken.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            ipady=7,
        )

        prozentanzeige = tk.Label(
            balkenbereich,
            text=f"{daten.ects_fortschritt:.0f} %",
            bg="#f7f7f7",
            font=("Segoe UI", 10),
            width=8,
            anchor="e",
        )
        prozentanzeige.pack(
            side=tk.RIGHT,
            padx=(12, 0),
        )

    def _erstelle_kennzahlenbereich(
        self,
        daten: DashboardDatenDTO,
    ) -> None:
        """Erstellt die drei Kennzahlenkarten."""

        kennzahlenbereich = tk.Frame(
            self._hauptbereich,
            bg="#f5f5f5",
        )
        kennzahlenbereich.pack(
            fill=tk.X,
            pady=(0, 15),
        )

        for spalte in range(3):
            kennzahlenbereich.columnconfigure(
                spalte,
                weight=1,
                uniform="kennzahlen",
            )

        notendurchschnitt = (
            f"{daten.notendurchschnitt:.2f}"
            if daten.notendurchschnitt > 0
            else "–"
        )

        self._erstelle_kennzahlkarte(
            parent=kennzahlenbereich,
            spalte=0,
            titel="Notendurchschnitt",
            wert=notendurchschnitt,
        )

        self._erstelle_kennzahlkarte(
            parent=kennzahlenbereich,
            spalte=1,
            titel="Bestandene Module",
            wert=str(len(daten.bestandene_module)),
        )

        self._erstelle_kennzahlkarte(
            parent=kennzahlenbereich,
            spalte=2,
            titel="Offene Module",
            wert=str(len(daten.offene_module)),
        )

    def _erstelle_kennzahlkarte(
        self,
        parent: tk.Frame,
        spalte: int,
        titel: str,
        wert: str,
    ) -> None:
        """Erstellt eine einzelne Kennzahlenkarte."""

        karte = tk.Frame(
            parent,
            bg="#ffffff",
            highlightbackground="#666666",
            highlightthickness=1,
            height=105,
        )
        karte.grid(
            row=0,
            column=spalte,
            padx=8,
            sticky="nsew",
        )
        karte.grid_propagate(False)

        titel_label = tk.Label(
            karte,
            text=titel,
            bg="#ffffff",
            font=("Segoe UI", 9, "bold"),
        )
        titel_label.pack(
            pady=(25, 2),
        )

        wert_label = tk.Label(
            karte,
            text=wert,
            bg="#ffffff",
            font=("Segoe UI", 19),
        )
        wert_label.pack()

    def _erstelle_aktuelle_module(
        self,
        daten: DashboardDatenDTO,
    ) -> None:
        """Erstellt die Liste der aktuell gebuchten Module."""

        bereich = self._erstelle_abschnitt(
            titel="Aktuell gebuchte Kurse",
        )

        listenrahmen = tk.Frame(
            bereich,
            bg="#f7f7f7",
        )
        listenrahmen.pack(
            fill=tk.BOTH,
            expand=True,
            padx=28,
            pady=(0, 15),
        )

        scrollbar = ttk.Scrollbar(
            listenrahmen,
            orient=tk.VERTICAL,
        )
        scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y,
        )

        modul_liste = tk.Listbox(
            listenrahmen,
            yscrollcommand=scrollbar.set,
            bg="#f7f7f7",
            borderwidth=0,
            highlightthickness=0,
            font=("Segoe UI", 10),
            activestyle="none",
            selectbackground="#d9d9d9",
            height=5,
        )
        modul_liste.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
        )

        scrollbar.configure(
            command=modul_liste.yview,
        )

        if daten.aktuelle_module:
            for modul in daten.aktuelle_module:
                modul_liste.insert(
                    tk.END,
                    f"• {modul.titel} ({modul.ects} ECTS)",
                )
        else:
            modul_liste.insert(
                tk.END,
                "Keine aktuell gebuchten Module",
            )

    def _erstelle_abschlussbereich(
        self,
        daten: DashboardDatenDTO,
    ) -> None:
        """Erstellt die Abschlussprognose und den Studienstatus."""

        bereich = self._erstelle_abschnitt(
            titel="Geplanter Studienabschluss",
        )

        abschlussdatum = daten.abschlussprognose.strftime(
            "%d.%m.%Y"
        )

        abschluss_label = tk.Label(
            bereich,
            text=f"Prognostizierter Abschluss: {abschlussdatum}",
            bg="#f7f7f7",
            font=("Segoe UI", 11),
            anchor="w",
        )
        abschluss_label.pack(
            fill=tk.X,
            padx=28,
            pady=(0, 4),
        )

        status_label = tk.Label(
            bereich,
            text=f"Status: {daten.studienstatus}",
            bg="#f7f7f7",
            font=("Segoe UI", 11),
            anchor="w",
        )
        status_label.pack(
            fill=tk.X,
            padx=28,
            pady=(0, 4),
        )

        zeit_label = tk.Label(
            bereich,
            text=f"Zeitfortschritt: {daten.zeitfortschritt:.1f} %",
            bg="#f7f7f7",
            font=("Segoe UI", 10),
            anchor="w",
        )
        zeit_label.pack(
            fill=tk.X,
            padx=28,
            pady=(0, 15),
        )

    def _erstelle_abschnitt(
        self,
        titel: str,
    ) -> tk.Frame:
        """Erstellt einen umrandeten Dashboard-Abschnitt."""

        bereich = tk.Frame(
            self._hauptbereich,
            bg="#f7f7f7",
            highlightbackground="#666666",
            highlightthickness=1,
        )
        bereich.pack(
            fill=tk.BOTH,
            expand=True,
            padx=38,
            pady=(0, 15),
        )

        titel_label = tk.Label(
            bereich,
            text=titel,
            bg="#f7f7f7",
            font=("Segoe UI", 14, "bold"),
            anchor="w",
        )
        titel_label.pack(
            fill=tk.X,
            padx=28,
            pady=(20, 8),
        )

        return bereich

    def _leere_hauptbereich(self) -> None:
        """Entfernt bereits vorhandene Oberflächenelemente."""

        for element in self._hauptbereich.winfo_children():
            element.destroy()

    @staticmethod
    def _begrenze_prozentwert(wert: float) -> float:
        """Begrenzt einen Prozentwert auf den Bereich von 0 bis 100."""

        return max(0.0, min(wert, 100.0))

    @staticmethod
    def _konfiguriere_stile() -> None:
        """Konfiguriert den Stil des Fortschrittsbalkens."""

        style = ttk.Style()

        if "clam" in style.theme_names():
            style.theme_use("clam")

        style.configure(
            "Dashboard.Horizontal.TProgressbar",
            troughcolor="#eeeeee",
            background="#a6a6a6",
            bordercolor="#555555",
            lightcolor="#a6a6a6",
            darkcolor="#a6a6a6",
        )