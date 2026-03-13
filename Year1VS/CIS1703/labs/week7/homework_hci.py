import tkinter as tk 

root = tk.Tk()
root.title("Unbreakable Login")
root.geometry("400x200")

def check_password():
    password = entered_password.get()
    if len(password) < 6:
        return feedback.config(text="Password must be at least 6 characters long.", bg="White", fg="Red")
    return feedback.config(text="Password accepted!", bg="Green", fg="White")

entered_password = tk.Entry(show="*", text="Password")
entered_password.pack(pady=10)
tk.Button(text="Submit", command=check_password).pack(pady=10)
feedback = tk.Label(bg="White")
feedback.pack(pady=10)


tk.mainloop()
