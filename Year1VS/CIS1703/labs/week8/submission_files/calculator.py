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

def calculate(operation):
    first_num, second_num = num1.get(), num2.get()
    try:
        first_num = float(first_num)
        second_num = float(second_num)
    except ValueError:
        display.config(text="Please enter a number (e.g. 5) into each of the two text boxes.")
        return
    
    if operation == '+':
        display.config(text=first_num + second_num)
    elif operation == '-':
        display.config(text=first_num - second_num)
    elif operation == "*":
        display.config(text=first_num * second_num)
    else:
        try:
            display.config(text=first_num / second_num)
        except ZeroDivisionError:
            display.config(text="Cannot divide by zero.")


root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")
root.config(bg="#8686f0")

container = tk.Frame(root)
container.pack(pady=10)

num1 = tk.Entry(container)
num1.grid(row=0, column=0)
num1.insert(0, 'Enter Number')
num1.bind('<FocusIn>', clear_num1)

num2=tk.Entry(container)
num2.grid(row=0, column=2)
num2.insert(0, 'Enter Number')
num2.bind('<FocusIn>', clear_num2)

operations = tk.Frame(container)
operations.grid(row=1, sticky="ew")

tk.Button(operations, text='+', command= lambda: calculate("+"), width=20).grid(row=0, column=0)
tk.Button(operations, text='-', command= lambda: calculate("-"), width=20).grid(row=0, column=1)
tk.Button(operations, text='/', command= lambda: calculate("/"), width=20).grid(row=1, column=0)
tk.Button(operations, text='*', command= lambda: calculate("*"), width=20).grid(row=1, column=1)


display = tk.Label(container, text="")
display.grid(row=2, columnspan=2)

tk.Button(container, text="Exit", bg="Red", fg="White", command=leave).grid(row=3, column=3)

root.mainloop()