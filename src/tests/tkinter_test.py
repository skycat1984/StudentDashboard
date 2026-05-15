import tkinter as tk
from tkinter import messagebox

# Funktion für den Button
def begruessung():
    messagebox.showinfo("Test", "Tkinter funktioniert erfolgreich!")

# Hauptfenster erstellen
fenster = tk.Tk()
fenster.title("Tkinter Test")
fenster.geometry("400x200")

# Überschrift
titel = tk.Label(
    fenster,
    text="Studien-Dashboard Test",
    font=("Arial", 16)
)
titel.pack(pady=20)

# Test-Button
button = tk.Button(
    fenster,
    text="Tkinter testen",
    command=begruessung
)
button.pack(pady=10)

# Fenster starten
fenster.mainloop()