"""
Service zur Berechnung des zeitlichen Studienfortschritts
und einer voraussichtlichen Abschlussprognose.

Der Service arbeitet ausschließlich mit übergebenen Werten und enthält
keine Datenbankzugriffe oder Darstellungslogik.
"""

import calendar
from datetime import date, timedelta


class AbschlussPrognoseService:
    """
    Berechnet den zeitlichen Studienfortschritt, prognostiziert ein
    Abschlussdatum und bewertet den aktuellen Studienstatus.
    """

    def berechne_zeitfortschritt(
        self,
        startdatum: date,
        anzahl_semester: int,
        stichtag: date | None = None,
    ) -> float:
        """
        Berechnet den prozentualen zeitlichen Studienfortschritt.

        Die vorgesehene Studiendauer wird aus der Anzahl der Semester
        berechnet. Ein Semester entspricht sechs Monaten.

        Args:
            startdatum:
                Datum des Studienbeginns.
            anzahl_semester:
                Anzahl der Semester des gewählten Studienmodells.
            stichtag:
                Datum, für das der Fortschritt berechnet wird.
                Ohne Angabe wird das heutige Datum verwendet.

        Returns:
            Zeitlicher Studienfortschritt zwischen 0.0 und 100.0 Prozent,
            gerundet auf zwei Nachkommastellen.

        Raises:
            ValueError:
                Wenn die Anzahl der Semester kleiner oder gleich null ist.
        """

        if anzahl_semester <= 0:
            raise ValueError(
                "Die Anzahl der Semester muss größer als null sein."
            )

        aktueller_stichtag = stichtag or date.today()

        regelstudienende = self._addiere_monate(
            startdatum,
            anzahl_semester * 6,
        )

        gesamte_studiendauer = (
            regelstudienende - startdatum
        ).days

        vergangene_studienzeit = (
            aktueller_stichtag - startdatum
        ).days

        if vergangene_studienzeit <= 0:
            return 0.0

        if aktueller_stichtag >= regelstudienende:
            return 100.0

        zeitfortschritt = (
            vergangene_studienzeit
            / gesamte_studiendauer
            * 100
        )

        return round(zeitfortschritt, 2)

    def prognostiziere_abschlussdatum(
        self,
        startdatum: date,
        anzahl_semester: int,
        ects_fortschritt: float,
        stichtag: date | None = None,
    ) -> date:
        """
        Prognostiziert das Abschlussdatum anhand des bisherigen ECTS-Tempos.

        Wenn noch keine ECTS erreicht wurden oder das Studium noch nicht
        begonnen hat, wird das reguläre Studienende zurückgegeben.

        Args:
            startdatum:
                Datum des Studienbeginns.
            anzahl_semester:
                Anzahl der Semester des gewählten Studienmodells.
            ects_fortschritt:
                Bisher erreichter ECTS-Fortschritt in Prozent.
            stichtag:
                Datum, auf dessen Grundlage die Prognose erfolgt.
                Ohne Angabe wird das heutige Datum verwendet.

        Returns:
            Voraussichtliches Abschlussdatum.

        Raises:
            ValueError:
                Wenn die Anzahl der Semester ungültig ist oder der
                ECTS-Fortschritt außerhalb von 0 bis 100 liegt.
        """

        if anzahl_semester <= 0:
            raise ValueError(
                "Die Anzahl der Semester muss größer als null sein."
            )

        if not 0.0 <= ects_fortschritt <= 100.0:
            raise ValueError(
                "Der ECTS-Fortschritt muss zwischen 0 und 100 liegen."
            )

        aktueller_stichtag = stichtag or date.today()

        regelstudienende = self._addiere_monate(
            startdatum,
            anzahl_semester * 6,
        )

        if ects_fortschritt >= 100.0:
            return aktueller_stichtag

        vergangene_tage = (
            aktueller_stichtag - startdatum
        ).days

        if vergangene_tage <= 0 or ects_fortschritt == 0.0:
            return regelstudienende

        fortschritt_pro_tag = (
            ects_fortschritt / vergangene_tage
        )

        verbleibender_fortschritt = (
            100.0 - ects_fortschritt
        )

        verbleibende_tage = round(
            verbleibender_fortschritt
            / fortschritt_pro_tag
        )

        return aktueller_stichtag + timedelta(
            days=verbleibende_tage
        )

    def ermittle_studienstatus(
        self,
        ects_fortschritt: float,
        zeitfortschritt: float,
    ) -> str:
        """
        Vergleicht ECTS- und Zeitfortschritt.

        Eine Abweichung von bis zu fünf Prozentpunkten gilt als
        planmäßiger Studienverlauf.

        Args:
            ects_fortschritt:
                Erreichter ECTS-Fortschritt in Prozent.
            zeitfortschritt:
                Verbrauchter Anteil der geplanten Studienzeit in Prozent.

        Returns:
            Einer der Werte:
            - "Vor dem Zeitplan"
            - "Im Zeitplan"
            - "Hinter dem Zeitplan"

        Raises:
            ValueError:
                Wenn ein Fortschrittswert außerhalb von 0 bis 100 liegt.
        """

        self._pruefe_prozentwert(
            ects_fortschritt,
            "ECTS-Fortschritt",
        )
        self._pruefe_prozentwert(
            zeitfortschritt,
            "Zeitfortschritt",
        )

        toleranz = 5.0
        abweichung = ects_fortschritt - zeitfortschritt

        if abweichung > toleranz:
            return "Vor dem Zeitplan"

        if abweichung < -toleranz:
            return "Hinter dem Zeitplan"

        return "Im Zeitplan"

    @staticmethod
    def _addiere_monate(
        ausgangsdatum: date,
        monate: int,
    ) -> date:
        """
        Addiert Monate zu einem Datum.

        Dabei werden unterschiedliche Monatslängen und Schaltjahre
        berücksichtigt.
        """

        monatsindex = (
            ausgangsdatum.month - 1 + monate
        )

        jahr = (
            ausgangsdatum.year
            + monatsindex // 12
        )

        monat = monatsindex % 12 + 1

        letzter_tag = calendar.monthrange(
            jahr,
            monat,
        )[1]

        tag = min(
            ausgangsdatum.day,
            letzter_tag,
        )

        return date(
            jahr,
            monat,
            tag,
        )

    @staticmethod
    def _pruefe_prozentwert(
        wert: float,
        bezeichnung: str,
    ) -> None:
        """Prüft, ob ein Wert zwischen 0 und 100 liegt."""

        if not 0.0 <= wert <= 100.0:
            raise ValueError(
                f"{bezeichnung} muss zwischen 0 und 100 liegen."
            )
        
