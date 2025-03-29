import tkinter as tk
from tkinter import scrolledtext
from .themes import Theme

class MainWindow:
    def __init__(self, title="NoteMaster"):
        self.root = tk.Tk()
        self.root.title(title)
        self.theme = Theme()
        self.setup_ui()

    def setup_ui(self):
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')

        self.apply_theme()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def apply_theme(self):
        current_theme = self.theme.get_current_theme()
        self.root.configure(bg=current_theme['background'])
        self.text_area.configure(bg=current_theme['background'], fg=current_theme['text_color'])

    def on_closing(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()
