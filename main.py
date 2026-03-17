import tkinter as tk

history = []


def convert():
    try:
        value = float(entry_value.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        # Umrechnung zuerst in Meter
        if from_unit == "Meter":
            meters = value
        elif from_unit == "Kilometer":
            meters = value * 1000
        elif from_unit == "Zentimeter":
            meters = value / 100

        # Von Meter in Ziel-Einheit
        if to_unit == "Meter":
            result = meters
        elif to_unit == "Kilometer":
            result = meters / 1000
        elif to_unit == "Zentimeter":
            result = meters * 100

        result_label.config(text=f"Ergebnis: {result:.4f}")

        # Historie hinzufügen
        history.append(f"{value} {from_unit} -> {result:.4f} {to_unit}")
        history[:] = history[-10:]  # Behalte nur die letzten 10
        listbox.delete(0, tk.END)
        for item in history:
            listbox.insert(tk.END, item)

    except ValueError:
        result_label.config(text="Bitte eine gültige Zahl eingeben")


root = tk.Tk()
root.title("Einheitenumrechner")
root.geometry("600x300")  # Breite erhöht für Layout

# Frames für Layout
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Eingabe
tk.Label(left_frame, text="Wert eingeben:").pack(pady=5)
entry_value = tk.Entry(left_frame)
entry_value.pack()

# Auswahl Ausgangseinheit
tk.Label(left_frame, text="Von Einheit:").pack(pady=5)
from_var = tk.StringVar(value="Meter")
from_menu = tk.OptionMenu(left_frame, from_var, "Meter", "Kilometer", "Zentimeter")
from_menu.pack()

# Auswahl Zieleinheit
tk.Label(left_frame, text="In Einheit:").pack(pady=5)
to_var = tk.StringVar(value="Kilometer")
to_menu = tk.OptionMenu(left_frame, to_var, "Meter", "Kilometer", "Zentimeter")
to_menu.pack()

# Button
convert_button = tk.Button(left_frame, text="Umrechnen", command=convert)
convert_button.pack(pady=10)

# Ergebnisanzeige
result_label = tk.Label(left_frame, text="Ergebnis:")
result_label.pack()

# Listbox für Historie
tk.Label(right_frame, text="Letzte Umrechnungen:").pack(pady=5)
listbox = tk.Listbox(right_frame, height=15)
listbox.pack(pady=5)

root.mainloop()