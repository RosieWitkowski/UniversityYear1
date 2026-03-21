import tkinter as tk
def show_selection():
    selected = []
    if python_var.get(): selected.append("Python")
    if java_var.get(): selected.append("Java")
    if js_var.get(): selected.append("JavaScript")
    if csharp_var.get(): selected.append("C#")

    if selected: 
        result_var.set("Selected: " + ", ".join(selected))
    else:
        result_var.set("No languages selected.")

root = tk.Tk()
root.title("Checkbuttons and Radiobuttons")
root.geometry("400x400")
# --- Checkbuttons section ---
tk.Label(root, text="Which languages do you know?",
font=("Arial", 12, "bold")).pack(pady=(15, 5))

python_var = tk.BooleanVar()
java_var = tk.BooleanVar()
js_var = tk.BooleanVar()
csharp_var = tk.BooleanVar()

tk.Checkbutton(root, text="Python", variable=python_var,
font=("Arial", 11)).pack(anchor="w", padx=40)

tk.Checkbutton(root, text="Java", variable=java_var,
font=("Arial", 11)).pack(anchor="w", padx=40)

tk.Checkbutton(root, text="JavaScript", variable=js_var,
font=("Arial", 11)).pack(anchor="w", padx=40)

tk.Checkbutton(root, text="C#", variable=csharp_var,
font=("Arial", 11)).pack(anchor="w", padx=40)

tk.Button(root, text="Show Selection", command=show_selection,
bg="#5B2C8E", fg="white").pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", 11),
fg="#5B2C8E", wraplength=350).pack(pady=5)

root.mainloop()