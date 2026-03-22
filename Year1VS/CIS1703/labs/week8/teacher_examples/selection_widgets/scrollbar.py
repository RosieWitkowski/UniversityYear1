import tkinter as tk
def add_item():
    item = entry.get().strip()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
        status_var.set(f"Added: {item}")

def remove_item():
    selection = listbox.curselection()
    if selection:
        item = listbox.get(selection[0])
        listbox.delete(selection[0])
        status_var.set(f"Removed: {item}")
    else:
        status_var.set("No item selected.")

def clear_all():
    listbox.delete(0, tk.END)
    status_var.set("All items cleared.")

root = tk.Tk()
root.title("Listbox Tutorial")
root.geometry("400x400")
# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10, padx=10, fill=tk.X)
entry = tk.Entry(input_frame, font=("Arial", 11))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
entry.bind("<Return>", lambda e: add_item())
tk.Button(input_frame, text="Add", command=add_item,
bg="#5B2C8E", fg="white").pack(side=tk.LEFT)
# Listbox with scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(
list_frame,
font=("Arial", 11),
selectmode=tk.SINGLE,
yscrollcommand=scrollbar.set,
activestyle="none"
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)
# Pre-populate with sample data
for item in ["Python", "Java", "C++", "JavaScript", "Ruby",
"Go", "Rust", "Swift", "Kotlin", "TypeScript"]:
    listbox.insert(tk.END, item)
# Action buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Remove Selected",
command=remove_item).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Clear All", command=clear_all,
fg="red").pack(side=tk.LEFT, padx=5)
# Status bar
status_var = tk.StringVar(value="Ready")
tk.Label(root, textvariable=status_var, relief="sunken",
anchor="w", font=("Arial", 10)).pack(fill=tk.X, padx=10, pady=(5, 10))
root.mainloop()