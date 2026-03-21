import tkinter as tk
root = tk.Tk()
root.title("Frames Demo -- Contact Card")
root.geometry("450x350")
root.configure(bg="#f0f0f0")
# Header frame
header = tk.Frame(root, bg="#5B2C8E", height=60)
header.pack(fill=tk.X)
header.pack_propagate(False)
tk.Label(header, text="Contact Manager", font=("Arial", 16, "bold"),
bg="#5B2C8E", fg="white").pack(expand=True)
# Form frame using grid layout
form = tk.Frame(root, bg="#f0f0f0")
form.pack(pady=20, padx=20, fill=tk.X)
fields = ["First Name", "Last Name", "Email", "Phone"]
entries = {}
for i, field in enumerate(fields):
    tk.Label(form, text=field + ":", font=("Arial", 11),
    bg="#f0f0f0").grid(row=i, column=0, pady=5, padx=5, sticky="e")
entry = tk.Entry(form, font=("Arial", 11), width=30)
entry.grid(row=i, column=1, pady=5, padx=5, sticky="w")
entries[field] = entry
# Button frame

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)
for text, colour in [("Save", "#5B2C8E"), ("Clear", "#666"),
("Cancel", "#CC3333")]:
    tk.Button(btn_frame, text=text, bg=colour, fg="white",
    font=("Arial", 10, "bold"), width=10).pack(side=tk.LEFT, padx=5)
# Status bar frame
status_frame = tk.Frame(root, bg="#ddd", height=25)
status_frame.pack(fill=tk.X, side=tk.BOTTOM)
status_frame.pack_propagate(False)
tk.Label(status_frame, text="Ready", font=("Arial", 9),
bg="#ddd", anchor="w").pack(fill=tk.X, padx=5)
root.mainloop()