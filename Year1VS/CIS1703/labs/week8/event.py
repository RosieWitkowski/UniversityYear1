# Uses events to make a label act like an entry
import tkinter as tk 

root = tk.Tk()
root.title("Events")
root.geometry("400x300")
root.config(bg="#570ff2")

def add_char(event):
    current_text = entry_mimic.cget("text") # cget gets configuration, this case 'text'
    entry_mimic.config(text=current_text+event.char)

def delete_char(event):
    current_text = entry_mimic.cget("text")
    entry_mimic.config(text=current_text[:-1])

entry_mimic = tk.Label(
    root,
    text="",
    fg="#f20ff2",
    font=("Arial", 20)
)
entry_mimic.pack(pady=10)

root.bind("<BackSpace>", delete_char)
root.bind("<Key>", add_char)

root.mainloop()