import sqlite3

# Verbindung zur Datenbank
connection = sqlite3.connect(":memory:")

# Cursor erstellen
cursor = connection.cursor()

# Tabelle erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matrikelnummer TEXT,
    name TEXT
)
""")

# Datensatz einfügen
cursor.execute("""
INSERT INTO student (matrikelnummer, name)
VALUES (?, ?)
""", ("123456", "Sabine Mustermann"))

# Änderungen speichern
connection.commit()

# Daten auslesen
cursor.execute("SELECT * FROM student")

daten = cursor.fetchall()

print("Gespeicherte Studenten:")

for student in daten:
    print(student)

# Verbindung schließen
connection.close()