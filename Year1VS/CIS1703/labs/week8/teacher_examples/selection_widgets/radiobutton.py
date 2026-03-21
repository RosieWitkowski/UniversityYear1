import tkinter as tk 

def show_difficulty():
    if difficulty_var.get(): display.config(text=f"Difficulty: {difficulty_var}")


root = tk.Tk()
root.geometry("400x300")

tk.Label(root, text="\nPreferred difficulty:",
font=("Arial", 12, "bold")).pack(pady=(10, 5))

difficulty_var = tk.StringVar(value="medium")

for text, value in [("Easy", "easy"), ("Medium", "medium"), ("Hard",
"hard")]:
    tk.Radiobutton(
    root,
    text=text,
    variable=difficulty_var,
    value=value,
    font=("Arial", 11),
    ).pack(anchor="w", padx=40)

tk.Button(
    root,
    text="Confirm difficulty",
    command=show_difficulty
).pack(pady=5)

display = tk.Label(
    root,
    text="Difficulty: "
)
display.pack(pady=10)

root.mainloop()