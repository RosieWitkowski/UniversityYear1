# Imporant Tips specific to layout managers
Max 1 layout manager per container - convention is to use pack() on frames, grid() within them
Use place() sparingly as static position means non-responsive
Use a class for reusability - in main use root = tk.Tk(), pass the root to the class, then root.mainloop()
Headers can fill width using .pack(fill= tk.X)
