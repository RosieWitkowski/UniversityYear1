import tkinter as tk 

root1 = tk.Tk()
root1.title("Window")
root1.geometry("100x200")
root1.resizable(False, True)
root1.configure(bg="Green")

label1 = tk.Label(
    root1,
    text="Label1"
)
label1.pack(pady=10)

label2 = tk.Label(
    root1,
    text= "Label2",
    font=("Comic Sans MS", 18, "bold"),
    bg = "Purple"
)
label2.pack(pady=50)

# Second window
root2 = tk.Tk()
root2.title("Window2")

label1 = tk.Label(
    root2,
    text="Label3"
)
label1.pack(pady=10)

# Other types of widgets
# Checkbutton, listbox, radiobutton, scale

tk.mainloop()