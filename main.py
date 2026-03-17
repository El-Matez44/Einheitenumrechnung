import tkinter as tk

formulas = []


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

        # Formel berechnen und zur Liste hinzufügen
        if value != 0:
            # Schritte anzeigen
            if from_unit != "Meter":
                formulas.append(f"{from_unit} --> Meter")
                if from_unit == "Kilometer":
                    factor1 = 1000
                elif from_unit == "Zentimeter":
                    factor1 = 0.01
                formulas.append(f"meter = {from_unit.lower()} * {factor1}")
                formulas.append(f"eingesetzt: meter = {value} * {factor1} = {meters}")

            if to_unit != "Meter":
                formulas.append(f"Meter --> {to_unit}")
                if to_unit == "Kilometer":
                    factor2 = 0.001
                elif to_unit == "Zentimeter":
                    factor2 = 100
                formulas.append(f"{to_unit.lower()} = meter * {factor2}")
                formulas.append(f"eingesetzt: {to_unit.lower()} = {meters} * {factor2} = {result}")

            formulas[:] = formulas[-30:]  # Behalte nur die letzten 30 (für mehr Einträge)
            listbox.delete(0, tk.END)
            for item in formulas:
                listbox.insert(tk.END, item)
        else:
            # Optional: Fehlermeldung in Listbox
            pass

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

# Listbox für Formeln
tk.Label(right_frame, text="Angewendete Formeln:").pack(pady=5)
listbox = tk.Listbox(right_frame, height=15, width=40)
listbox.pack(pady=5)

root.mainloop()