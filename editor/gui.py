import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Text Editor")
        self.geometry("800x600")

        self._create_menu_bar()

    def _create_menu_bar(self):
        menubar = tk.Menu(self)


