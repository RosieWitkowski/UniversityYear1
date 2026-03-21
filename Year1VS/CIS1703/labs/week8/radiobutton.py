import tkinter as tk 

def greet():
    lang = language.get()

    if lang == 'English':
        display.config(text="Hello!")
    elif lang == 'French':
        display.config(text="Bonjour!")
    else:
        display.config(text="Hola!")

root = tk.Tk()
root.title("Radiobutton")
root.geometry("400x300")
root.config(bg="#59dac3")

tk.Label(root, text="Please select a language.").pack(pady=10)

language = tk.StringVar(value='English')
tk.Radiobutton(root, text="English", variable=language, value="English").pack(pady=2)
tk.Radiobutton(root, text="French", variable=language, value="French").pack(pady=2)
tk.Radiobutton(root, text="Spanish", variable=language, value="Spanish").pack(pady=2)

display = tk.Label(root, text="")
display.pack(pady=5)
tk.Button(root, text="Greet", command=greet).pack(pady=5)

root.mainloop()