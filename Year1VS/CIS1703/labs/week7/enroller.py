import tkinter as tk 

# Making a window
root = tk.Tk()
root.title("New Window")
root.geometry("400x300") # Width x Height
root.config(bg="#C88FDB") # Config alters existing widgets

# Adding labels (text)
tk.Label(
    root, # First argument is parent window
    text="CIS1703 Programming 2",
).pack(pady=10)

tk.Label(
    root,
    text="Welcome to CIS1703",
    font=("Times New Roman", 18, "italic"),
    bg="Black", # Background colour
    fg="White" # Foreground colour (text)
).pack(pady=20)

# Button (clickable widget, basis of event-driven programming)
is_enrolled, presses = 0, 0
def enroll():
    student_name = name.get() # Use get to read from an Entry widget
    student_name = student_name.strip()
    if not student_name:
        return display.config(text="Please enter a name.", fg="Red")
    if [char for char in student_name if char.isdigit()]: # Will only populate if False exists
        return display.config(text="Name cannot include numbers.", fg="Red")

    global is_enrolled, presses # Use global to ensure global var is altered, not shadow (Unbound local error)
    presses += 1
    # Fns usually above GUIs, here for task chronological order
    if is_enrolled == 0:
        display.config(text=f"Successfully enrolled {student_name}!\nButton presses: {presses}", fg="Green") # Updates label 
        is_enrolled  = 1
    else:
        display.config(text=f"Unenrolled {student_name}!\nButton presses: {presses}", fg="Red")
        is_enrolled = 0

    # Clear entry field after
    name.delete(0, tk.END)

def reset():
    global is_enrolled, presses
    is_enrolled, presses = 0, 0
    display.config(text="", fg="#C88FDB")
    
name = tk.Entry(
    root,
    width=30
)
name.pack(pady=10)

tk.Button(
    root,
    text="Click to enroll",
    command=enroll # Connects button to fn Doesnt use () to avoid calling immediately 
).pack(pady=10)

tk.Button(
    root,
    text="RESET",
    bg="Red",
    command=reset
).pack(pady=10)

display = tk.Label(root, font=("Comic Sans MS", 12), bg="#C88FDB")
display.pack(pady=10)

root.mainloop() # Required to keep window open and listening for events

