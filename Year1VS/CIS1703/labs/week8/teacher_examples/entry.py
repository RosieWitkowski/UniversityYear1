"""Teacher's example of basic GUI, binding to entry, common entry arguments"""

import tkinter as tk
def calculate_bmi():
    """Calculate BMI from user input."""
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if height <= 0 or weight <= 0:
            raise ValueError
        bmi = weight / (height ** 2)
        result_var.set(f"Your BMI is: {bmi:.1f}") # Uses tk StringVar to automatically update

        # Change colour based on BMI range
        if bmi < 18.5:
            result_label.config(fg="blue")
        elif bmi < 25:
            result_label.config(fg="green")
        elif bmi < 30:
            result_label.config(fg="orange")
        else:
            result_label.config(fg="red")
    except ValueError: # Catches try-except if not float, also raised ValueError for if height <=0...
        result_var.set("Please enter valid numbers.")
        result_label.config(fg="red")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x250")
root.configure(bg="#f5f5f5")

# Weight input
tk.Label(root, text="Weight (kg):", font=("Arial", 11),
bg="#f5f5f5").pack(pady=(15, 2))

weight_entry = tk.Entry(root, font=("Arial", 12), width=20,
justify="center")
weight_entry.pack()

weight_entry.insert(0, "e.g. 70")

# Height input
tk.Label(root, text="Height (m):", font=("Arial", 11),
bg="#f5f5f5").pack(pady=(10, 2))

height_entry = tk.Entry(root, font=("Arial", 12), width=20,
justify="center")
height_entry.pack()

height_entry.insert(0, "e.g. 1.75") # Inserts default text

# Focus events to clear placeholder text
def clear_weight(event): # Clear default text
    if weight_entry.get() == "e.g. 70":
        weight_entry.delete(0, tk.END)

def clear_height(event):
    if height_entry.get() == "e.g. 1.75":
        height_entry.delete(0, tk.END)

weight_entry.bind("<FocusIn>", clear_weight) # Binds to focus on entry, clear default text
height_entry.bind("<FocusIn>", clear_height)

# Calculate button
tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="#5B2C8E",
    fg="white",
    font=("Arial", 11, "bold")
).pack(pady=15)

# Result
result_var = tk.StringVar()  # Uses tk StringVar to automatically update

result_label = tk.Label(
    root,
    textvariable=result_var,  # Uses tk StringVar to automatically update
    font=("Arial", 13, "bold"),
    bg="#f5f5f5"
)
result_label.pack()

root.mainloop()