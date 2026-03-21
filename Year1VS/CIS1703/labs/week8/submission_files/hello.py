"""
Create a GUI application with the following requirements:
1. A window titled "Hello GUI" with a size of 400x200 pixels.
2. A Label that displays "Welcome to CIS1703!" in 16pt bold Arial, coloured purple.
3. An Entry widget where the user can type their name.
4. A Button labelled "Say Hello" that, when clicked, changes the label text to
"Hello, [name]!" using the name from the Entry.
5. A "Clear" button that resets the label and clears the Entry
"""
import tkinter as tk 

def greet():
    name = name_entry.get()
    if name:
        display.config(text=f"Hello, {name}!")
    else:
        display.config(text=f"Please enter a name.")

def clear():
    name_entry.delete(0, tk.END)
    display.config(text="")

root = tk.Tk()
root.title("Hello GUI")
root.geometry("400x200")

tk.Label(root, text="Welcome to CIS1703!", font=("Arial", 16, "bold"), bg="Purple").pack(pady=5)
name_entry = tk.Entry(root)
tk.Button(root, text="X", bg="Red", fg="White", command=exit, width=5).pack(side="right", pady=5)
display = tk.Label(root, text="")
display.pack(padx=5)
name_entry.pack(side="left", padx=5)
tk.Button(root, text="Say Hello", command=greet).pack(side="left", padx=5)
tk.Button(root, text="Clear", command=clear).pack(side="left", padx=5)

root.mainloop()