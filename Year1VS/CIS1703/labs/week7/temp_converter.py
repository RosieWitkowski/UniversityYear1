import tkinter as tk 

root = tk.Tk()
root.title("TemperatureConvertor")
root.geometry("400x300")
root.config(bg="#9b8acc")

def convert():
    result.config(bg="White")
    try:
        farenheit = float(entry.get())
        celcius = (farenheit - 32) * 5 / 9
        result.config(text=f"{celcius:.2f} C", fg="Black")
    except ValueError:
        result.config(text="Error: Please enter a number", fg="Red")

tk.Label(root, text="Temperature Converter (F -> C)", font=("Times New Roman", 18)).pack(pady=(15, 5))
entry = tk.Entry(root, font=("Times New Roman", 12), justify="center")
entry.pack(pady=5)
tk.Button(root, command=convert, text="Convert", font=("Arial", 12)).pack(pady=5)
result = tk.Label(root, font=("Arial", 12), bg="#9b8acc")
result.pack(pady=10)



tk.mainloop()