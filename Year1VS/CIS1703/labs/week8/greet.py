import tkinter as tk 

def greet():
    if name.get():
        display.config(text=f"Hello, {name.get()}!")
    else:
        display.config(text="!! Please enter a name !!")

root = tk.Tk()
root.title("Greeting")
root.geometry("400x300")

container = tk.Frame(root)
container.pack() # Defaults to middle

tk.Label(container, text="Greeter").grid(row=0, column=0, rowspan=True) 
name = tk.Entry(container)
name.grid(row=1, column=0)
tk.Button(container, text="Submit", command=greet).grid(row=1, column=1)
display = tk.Label(container, text="")
display.grid(row=2, columnspan=2)

root.mainloop()