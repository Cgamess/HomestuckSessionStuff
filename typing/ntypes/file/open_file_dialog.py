import tkinter as tk
from tkinter import filedialog

tkroot = tk.Tk()
tkroot.withdraw()

def open_file_dialog(types=[("PNG files", "*.png")], title="Image"):
    file_path = filedialog.askopenfilename(filetypes=types, title=title)
    return file_path

def save_file_dialog(types=[("PNG files")], title="Save Image", fileExtenstion=".png"):
    file_path = filedialog.asksaveasfilename(filetypes=types, title=title, defaultextension=fileExtenstion)
    return file_path