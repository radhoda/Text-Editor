import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Text Editor")
        self.geometry("800x600")

        self._create_menu_bar()
        self._create_text_box()

    def _create_menu_bar(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)

        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save As")
        file_menu.add_separator()
        file_menu.add_command(label="Exit")

        menubar.add_cascade(label="File", menu=file_menu)

        self.config(menu=menubar)

    def _create_text_box(self):
        self.text_area = tk.Text(self, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill=tk.BOTH)

