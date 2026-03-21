"""
Three Scale (slider) widgets for Red, Green, and Blue values (each ranging from
0 to 255).
2. A large Label or Frame that previews the selected colour in real time as sliders
move.
3. A Label displaying the hex colour code (e.g. #FF5733).
4. A "Copy Hex" button that copies the hex code to a Label or status bar.
5. Use the Scale widget’s command parameter to call an update function
whenever a slider changes."""

import tkinter as tk 
from tkinter import messagebox

def update_colour(colour):
    r,g,b = red.get(), green.get(), blue.get()
    hex_colour = f"#{r:02x}{g:02x}{b:02x}"
    root.config(bg=hex_colour)
    display.config(text=hex_colour)

def copy():
    text = display.cget('text')
    if not text:
        display.config(text="No colour selected, please use the above sliders to pick a colour.")
        return 
    root.clipboard_clear()
    root.clipboard_append(text)
    

def leave():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to exit?")
    if confirm:
        root.destroy()

root = tk.Tk()
root.title("Colour Changer")
root.geometry("400x400")

red = tk.Scale(root, from_=0, to=255, orient="horizontal", command= update_colour, bg="Red", label="R")
red.pack(pady=5)
green = tk.Scale(root, from_=0, to=255, orient="horizontal", command= update_colour, bg="Green", label="G")
green.pack(pady=5)
blue = tk.Scale(root, from_=0, to=255, orient="horizontal", command= update_colour, bg="Blue", label="B")
blue.pack(pady=5)

buttons_container = tk.Frame(root)
buttons_container.pack(pady=5)

display = tk.Label(buttons_container, text="")
display.grid(row=0, column=0)
tk.Button(buttons_container, text="Copy to clipboard", command=copy).grid(row=0, column=1)
tk.Button(buttons_container, text="Exit", bg="Red", fg="White", command=leave).grid(row=1, column=2)

root.mainloop()