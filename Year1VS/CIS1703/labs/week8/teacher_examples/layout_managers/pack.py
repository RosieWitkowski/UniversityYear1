import tkinter as tk
root = tk.Tk()
root.title("pack() Demo")
root.geometry("400x300")
# Widgets stack vertically by default
tk.Label(root, text="Top", bg="lightblue", width=30).pack(pady=5)
tk.Label(root, text="Middle", bg="lightgreen", width=30).pack(pady=5)
tk.Label(root, text="Bottom", bg="lightyellow", width=30).pack(pady=5)

"""tk.Button(root, text="Left").pack(side=tk.LEFT, padx=5)
tk.Button(root, text="Centre").pack(side=tk.LEFT, padx=5)
tk.Button(root, text="Right").pack(side=tk.LEFT, padx=5)"""

# Using side= to arrange horizontally
frame = tk.Frame(root)
frame.pack(pady=20)
tk.Button(frame, text="Left").pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Centre").pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Right").pack(side=tk.LEFT, padx=5)
# fill and expand options
tk.Label(root, text="Expanded", bg="salmon").pack(fill=tk.X, expand=True)
root.mainloop()