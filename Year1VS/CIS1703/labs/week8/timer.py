# Quick experiment, not from seminar
import tkinter as tk 
from time import sleep

root = tk.Tk()
root.title("Quick Clock Test")
root.geometry("400x300")
root.config(bg="Light Blue")


def countdown():
    global time, timer_ID
    
    display.config(text=time)
    start.config(state="disabled")
    time += 1
    root.update()

    timer_ID = display.after(1000, countdown) # Use after rather than a while True loop, as this would prevent mainloop() being reached


def close():
    root.destroy()
    root.after_cancel(timer_ID)
    

time = 0
display = tk.Label(
    root,
    text="0"
)
display.pack(pady=10)

start = tk.Button(
    root,
    text="START",
    command=countdown
)
start.pack(pady=10)

exit = tk.Button(
    root,
    text="EXIT",
    command=close
)
exit.pack(pady=10)

root.mainloop()
