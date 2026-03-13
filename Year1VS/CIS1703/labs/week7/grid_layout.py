import tkinter as tk 

def enroll():
    name, course = name_entry.get(), course_entry.get()
    if not name and course: 
        result.config(text="Error: Plase fill in all fields.", fg="Red")
    else:
        result.config(text=f"Successfully enrolled {name} on course {course}!\nCongratulations!", fg="Green")

def clear():
    name_entry.delete(0, tk.END) # Delete is used to remove text from entry widget
    course_entry.delete(0, tk.END)
    result.config(text="") # Config is used to alter (label's) existing properties

root = tk.Tk()
root.title("Enroller")
root.geometry("400x300")
root.config(bg="#61bbe9")

# Name label and entry
tk.Label(
    root,
    text="Student's name"
).grid(row=0, column=0, padx=10, pady=10, sticky="e") # First row, first column (Stick East, cell margin 10)

name_entry = tk.Entry(
    root
)
name_entry.grid(row=0, column=1, padx=10, pady=10) # First row, second column

# Course label and entry
tk.Label(
    root,
    text="Course"
).grid(row=1, column=0, padx=10, pady=10, sticky="e") # Second row, first column

course_entry = tk.Entry( 
    root
)
course_entry.grid(row=1, column=1, padx=10, pady=10,) # Second row, second column

# Submit and clear buttons
tk.Button(
    root,
    text="Enroll",
    command=enroll # Esure no () so doesn't run on start
).grid(row=2, column=0, columnspan=2, pady=15) # Third row, first column
tk.Button(
    root,
    text="Clear",
    command=clear
).grid(row=2, column=1)

# Result display
result = tk.Label(
    root,
    fg="Black",
    bg="#61bbe9"
)
result.grid(row=3, column=0, columnspan=2) # Fourth row, spans 2 columns

# Keep window open
root.mainloop()