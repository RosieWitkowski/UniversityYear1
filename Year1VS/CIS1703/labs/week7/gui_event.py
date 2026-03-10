import tkinter as tk 

root = tk.Tk()
root.title("PokemonNamer.io")
root.geometry("400x600")
root.resizable(False, False)
root.config(bg="Yellow")

def guess():
    guess = entry.get()
    if not guess:
        return result.config(text="ERROR: Please enter a guess!", fg="Red")
        
    if guess.lower() in['pikachu', 'psyduck', 'mimikyu']:
        result.config(text=f"That's right, it's {guess}!", fg="Green")
    else:
        result.config(text="Incorrect!", fg="Red")

tk.Label(root, text="Name that pokemon!", font=("Comic Sans MS", 18), bg="Yellow").pack(pady=20)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=20)
tk.Button(root, text="Guess", command=guess, font=("Arial, 12")).pack(pady=10)
result = tk.Label(root, text="", font=("Comic Sans MS", 18), bg="Yellow")
result.pack(pady=25)

tk.mainloop()