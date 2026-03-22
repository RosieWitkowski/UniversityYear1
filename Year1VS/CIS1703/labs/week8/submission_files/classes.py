# Quick example layout of using classes and mainloop with GUI

import tkinter as tk 
from tkinter import messagebox

class Checklist():
    def __init__(self, root):
        self.root = root
        self.root.title("Checklist")
        self.root.geometry("400x300")
        self.root.config(bg="#6591ff")

if __name__ == "__main__":
    root = tk.Tk()
    checklist = Checklist(root)
    root.mainloop()