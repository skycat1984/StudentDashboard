"""
Service zur Berechnung des Notendurchschnitts.

Der Service verarbeitet bereits geladene Prüfungsergebnisse und enthält
keine Datenbankzugriffe oder Darstellungslogik.
"""

from ..domain.enums import Pruefungsstatus
from ..domain.pruefungsergebnis import Pruefungsergebnis


class NotenService:
    """Berechnet den Notendurchschnitt eines Studenten."""

    def berechne_notendurchschnitt(
        self,
        pruefungsergebnisse: list[Pruefungsergebnis],
    ) -> float:
        """
        Berechnet den Durchschnitt aller bestandenen Prüfungen.

        Berücksichtigt werden ausschließlich Prüfungsergebnisse mit dem
        Status BESTANDEN und einer vorhandenen Note.

        Args:
            pruefungsergebnisse:
                Prüfungsergebnisse des Studenten.

        Returns:
            Arithmetischer Notendurchschnitt, gerundet auf zwei
            Nachkommastellen. Sind noch keine bestandenen Prüfungen
            vorhanden, wird 0.0 zurückgegeben.
        """

        bestandene_noten = [
            ergebnis.note
            for ergebnis in pruefungsergebnisse
            if (
                ergebnis.status == Pruefungsstatus.BESTANDEN
                and ergebnis.note is not None
            )
        ]

        if not bestandene_noten:
            return 0.0

        durchschnitt = sum(bestandene_noten) / len(bestandene_noten)

        return round(durchschnitt, 2)
