import tkinter as tk
from tkinter import messagebox

def leave():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to exit?")
    if confirm:
        root.destroy()

def clear_num1(event):
    num1.delete(0, tk.END)

def clear_num2(event):
    num2.delete(0, tk.END)

def add():
    pass

def minus():
    pass

def divide():
    pass

def multiply():
    pass

root = tk.Tk()
root.title("Calculator")
root.geometry("400x300")
root.config(bg="#8686f0")

container = tk.Frame(root)
container.pack()

num1 = tk.Entry(container)
num1.grid(row=0, column=0)
num1.insert(0, 'Enter Number')
num1.bind('<FocusIn>', clear_num1)

num2=tk.Entry(container)
num2.grid(row=0, column=2)
num2.insert(0, 'Enter Number')
num2.bind('<FocusIn>', clear_num2)

operations = tk.Frame(container)
operations.grid(row=1, columnspan=2)

tk.Button(operations, text='+', command=add).pack(side='left', padx=5)
tk.Button(operations, text='-', command=minus).pack(side='left', padx=5)
tk.Button(operations, text='/', command=divide).pack(side='left', padx=5)
tk.Button(operations, text='*', command=multiply).pack(side='left', padx=5)

display = tk.Label(container, text="")
display.grid(row=2, columnspan=2)

tk.Button(container, text="Exit", bg="Red", fg="White", command=leave).grid(row=3, column=3)

root.mainloop()