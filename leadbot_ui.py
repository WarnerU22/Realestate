import threading
import tkinter as tk
from tkinter import messagebox

import autopilot_leadbot
from config import load_config, save_config


class LeadbotUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Leadbot Configuration")
        self.config_data = load_config()
        self.entries = {}
        row = 0
        for key, value in self.config_data.items():
            tk.Label(self, text=key).grid(row=row, column=0, sticky="e")
            entry = tk.Entry(self, width=40)
            if isinstance(value, list):
                entry.insert(0, ",".join(value))
            else:
                entry.insert(0, str(value))
            entry.grid(row=row, column=1, padx=5, pady=2)
            self.entries[key] = entry
            row += 1
        tk.Button(self, text="Save", command=self.save).grid(row=row, column=0, pady=5)
        tk.Button(self, text="Run", command=self.run_bot).grid(row=row, column=1, pady=5)

    def save(self):
        for key, entry in self.entries.items():
            val = entry.get()
            if key == "regions":
                val = [v.strip() for v in val.split(",") if v.strip()]
            elif key == "discount_threshold":
                val = float(val)
            self.config_data[key] = val
        save_config(self.config_data)
        messagebox.showinfo("Leadbot", "Configuration saved")

    def run_bot(self):
        self.save()
        threading.Thread(target=autopilot_leadbot.main, daemon=True).start()
        messagebox.showinfo("Leadbot", "Leadbot started in background")


if __name__ == "__main__":
    app = LeadbotUI()
    app.mainloop()
