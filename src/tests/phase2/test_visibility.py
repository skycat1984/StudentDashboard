"""
Testprogramm zur Untersuchung von Kapselung und Sichtbarkeit in Python.

Gezeigt werden öffentliche Attribute, interne Attribute nach Konvention,
Name Mangling sowie der kontrollierte Zugriff über eine Property.
"""


class Student:
    """Repräsentiert einen Studenten mit unterschiedlich sichtbaren Attributen."""

    def __init__(self, matrikelnummer: str, name: str) -> None:
        self.matrikelnummer = matrikelnummer    # Öffentliches Attribut
        self._name = name                       # Internes Attribut nach Konvention
        self.__interne_notiz = "Testnotiz"      # Attribut mit Name Mangling

    @property
    def name(self) -> str:
        """Gibt den Namen des Studenten zurück."""
        return self._name

    @name.setter
    def name(self, neuer_name: str) -> None:
        """Ändert den Namen, sofern dieser nicht leer ist."""
        if not neuer_name.strip():
            raise ValueError("Der Name darf nicht leer sein.")

        self._name = neuer_name


def main() -> None:
    """Führt die einzelnen Tests zu Sichtbarkeit und Kapselung aus."""

    student = Student("32209222", "Max Mustermann")

    # Zugriff auf ein öffentliches Attribut
    print("1. Öffentliches Attribut")
    print(student.matrikelnummer)

    # Lesen über die Property
    print("\n2. Zugriff über die Property")
    print(student.name)

    # Kontrollierte Änderung über den Property-Setter
    print("\n3. Änderung über den Property-Setter")
    student.name = "Anna Muster"
    print(student.name)

    # Der Setter verhindert einen leeren Namen
    print("\n4. Ungültige Änderung über den Property-Setter")
    try:
        student.name = "   "
    except ValueError as fehler:
        print(f"Fehler: {fehler}")

    # Direkter Zugriff auf _name bleibt trotz Konvention möglich
    print("\n5. Direkter Zugriff auf das interne Attribut")
    student._name = ""
    print(f"Direkt gesetzter Wert: '{student._name}'")
    print("Die Validierung der Property wurde umgangen.")

    # Direkter Zugriff auf __interne_notiz ist nicht möglich
    print("\n6. Zugriff auf ein Attribut mit doppeltem Unterstrich")
    try:
        print(student.__interne_notiz)
    except AttributeError as fehler:
        print(f"Direkter Zugriff nicht möglich: {fehler}")

    # Zugriff über den durch Name Mangling erzeugten Attributnamen
    print("\n7. Zugriff über den veränderten Attributnamen")
    print(student._Student__interne_notiz)


if __name__ == "__main__":
    main()
