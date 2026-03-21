import tkinter as tk 
from tkinter import messagebox 

root = tk.Tk()
root.title("Messages")
root.geometry("400x300")

# messagebox.showinfo("You've got mail!", "Hello!")
# messagebox.showwarning("You've got mail!", "Hello!")
# messagebox.showerror("You've got mail!", "Hello!")
# messagebox.askquestion("You've got mail!", "Hello!")
# messagebox.askyesno("You've got mail!", "Hello!")
messagebox.askokcancel("You've got mail!", "Hello!")

root.mainloop()