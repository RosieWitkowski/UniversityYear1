import tkinter as tk

def update_display():
    if not laundry_var.get() or not clean_var.get():
        display.config(text="Stinky!", bg="Red")
    else:
        display.config(text="Clean!", bg="Green")

root = tk.Tk()
root.title("Checklist")
root.geometry("400x300")
root.config(bg="#e7c940")

tk.Label(root, text="Your Checklist", bg="#d7e23e").pack(pady=5)

cook_var = tk.IntVar()
cook = tk.Checkbutton(root, text="Cook", variable=cook_var) 
cook.pack()

clean_var = tk.IntVar()
clean = tk.Checkbutton(root, text="Clean", variable=clean_var) 
clean.pack()

laundry_var = tk.IntVar()
laundry = tk.Checkbutton(root, text="Laundry", variable=laundry_var) 
laundry.pack()

shop_var = tk.IntVar()
shop = tk.Checkbutton(root, text="Shop", variable=shop_var) 
shop.pack(pady=5)

display = tk.Label(root, text="")
display.pack(pady=10)

tk.Button(root, text="Evaluate", command=update_display).pack()

root.mainloop()




"""
for chore in chores:
    chore_var = tk.IntVar()
    tk.Checkbutton(root, text=chore, variable=chore_var).pack() 

objectives_vars = []
objecties = []

for chore in chores:
    objectives_vars.append({f"{chore}": tk.IntVar()})
    objecties.append({f"{chore}": tk.Checkbutton(root, text=f"{chore}", variable=objectives_vars[f"{chore}"])})"""