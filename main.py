# Importing tkinter for UI purposes
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as messagebox

# Importing os
import os


class Settings:
    def __init__(self):
        self.title_main = "Installer Wizard"
        self.width = 800
        self.height = 500

        self.choose_exe_text = "Choose the .exe file"


settings = Settings()


class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(settings.title_main)

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.root.geometry(
            f"{settings.width}x{settings.height}+{self.screen_width - (self.screen_width - (settings.width // 2))}+{self.screen_height - (self.screen_height - (settings.height // 2)) - 100}")

        self.heading_label = tk.Label(self.root, text=settings.title_main, font="Calibri 16")
        self.heading_label.place(x=150, y=25)

        self.options_frame = tk.LabelFrame(self.root, text="Installer Options", width=500, height=250)
        self.options_frame.grid_propagate(False)
        self.options_frame.place(x=150, y=100)

        self.choose_exe_button = ttk.Button(self.options_frame, text=settings.choose_exe_text, command=self.input_file)
        self.choose_exe_button.grid(row=0, column=0, padx=75, pady=50)

        self.exe_path = tk.Label(self.options_frame, text="no file selected")
        self.exe_path.grid(row=1, column=0)

        self.desktop_shortcut_var = tk.IntVar()
        self.desktop_shortcut_var.set(0)
        self.desktop_shortcut_checkbox = tk.Checkbutton(self.options_frame, text="Include Desktop Shortcut",
                                                        offvalue=0, onvalue=1)
        self.desktop_shortcut_checkbox.select()
        self.desktop_shortcut_checkbox.grid(row=0, column=1)

        self.start_shortcut_var = tk.IntVar()
        self.start_shortcut_var.set(0)
        self.start_shortcut_checkbox = tk.Checkbutton(self.options_frame, text="Include Start Shortcut",
                                                      offvalue=0, onvalue=1)
        self.start_shortcut_checkbox.select()
        self.start_shortcut_checkbox.grid(row=1, column=1)

        self.generate_button = ttk.Button(self.root, text="Generate Shortcuts", command=self.generate_shortcuts)
        self.generate_button.place(x=325, y=400)

    def input_file(self):
        self.root.filename = filedialog.askopenfilename(initialdir="/", title="Select your .exe file",
                                                        filetypes=((".exe files", ".exe"), ("All Files", "*.*")))
        self.exe_path.config(text=os.path.basename(self.root.filename))

    def generate_shortcuts(self):
        if self.exe_path.cget("text") == "" or "no file selected":
            messagebox.showerror("Error", "No .exe file selected")

    def run(self):
        self.root.mainloop()


main = Main()
main.run()
