import tkinter as tk 

root = tk.Tk()
root.title("TemperatureConvertor")
root.geometry("400x300")
root.config(bg="#9b8acc")

def convert():
    setting = mode.get()
    if not setting:
        return result.config(text="Please choose a setting.", fg="Red", width=100)
    degrees = entry.get()
    if not degrees:
        return result.config(text="Please enter a number.", fg="Red", width=100)
    degrees = float(degrees)

    try:
        if setting == 'F':
            ans = (degrees - 32) * 5 / 9
        else:
            ans = (degrees * 9/5) + 32

        result.config(text=f"{ans:.2f} C", fg="Black", width=15)
    except ValueError:
        result.config(text="Error: Please enter a number", fg="Red", width=100)

def clear():
    entry.delete(0, tk.END)
    result.config(text="")


tk.Label(root, text="Temperature Converter (F -> C)", font=("Times New Roman", 18)).pack(pady=(15, 5))

# Setting
mode = tk.StringVar()
faren = tk.Radiobutton(root, variable=mode, text="F->C", value="F").pack(pady=10)
celc = tk.Radiobutton(root, variable=mode, text="C->F", value="C").pack(pady=10)

# Value to convert
entry = tk.Entry(root, font=("Times New Roman", 12), justify="center")
entry.pack(pady=5)
tk.Button(root, command=convert, text="Convert", font=("Arial", 12)).pack(pady=5)

# Display
result = tk.Label(root, font=("Arial", 12), width=10)
result.pack(pady=10)

# Clear option
tk.Button(root, command=clear, text="Clear").pack(pady=5)

tk.mainloop()