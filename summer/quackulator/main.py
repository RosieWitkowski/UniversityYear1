import tkinter as tk 
from winsound import PlaySound

root = tk.Tk()
root.title("Quackulator")
root.geometry("640x480")

border = {'highlightbackground': 'black', 'highlightthickness': '1'}
theme1= {'bg': "#6167A3", 'fg': "#FFFFFF", 'font': ('Courier New', 28), **border}
theme2= {'bg': "#FFB799", 'fg': "#000000", 'font': ('Courier New', 18), **border}
theme3 = {'bg': "#B7B5FF", 'fg': "#000000", 'font': ('Courier New', 24), **border}
theme4 = {'bg': "#9E9DDD", 'fg': "#000000", 'font': ('Courier New', 24), **border}

calc_border = tk.Frame(root, height=600, width=450)
calc_border.pack(pady=5)
calc_border.config(**border)

calc_frame = tk.Frame(calc_border)
calc_frame.pack(pady=15, padx=15)

# Output
output_display = tk.Label(calc_frame, text="2+2=4", **theme1, width=15, anchor='w')
output_display.grid(row=0, column=0, columnspan=4)

# Clear and backspace
clear_btn = tk.Button(calc_frame, **theme2, text="C")
clear_btn.grid(row=1, column=2)
back_btn = tk.Button(calc_frame, **theme2, text="<-")
back_btn.grid(row=1, column=3)

# Numbers and functions
# Row 0 (overall 3)
num1 = tk.Button(calc_frame, **theme3, text='7')
num1.grid(row=3, column=0)
num8 = tk.Button(calc_frame, **theme3, text='8')
num8.grid(row=3, column=1 )
num9 = tk.Button(calc_frame, **theme3, text='9')
num9.grid(row=3, column=2 )

divide_btn = tk.Button(calc_frame, **theme4, text='/')
divide_btn.grid(row=3, column=3)

# Row 1 (overall 4)
num4 = tk.Button(calc_frame, **theme3, text='4')
num4.grid(row=4, column=0 )
num5 = tk.Button(calc_frame, **theme3, text='5')
num5.grid(row=4, column=1 )
num6 = tk.Button(calc_frame, **theme3, text='6')
num6.grid(row=4, column=2 )

multiply_btn = tk.Button(calc_frame, **theme4, text='*')
multiply_btn.grid(row=4, column=3 )

# Row 2 (overall 5)
num1 = tk.Button(calc_frame, **theme3, text='1')
num1.grid(row=5, column=0)
num2 = tk.Button(calc_frame, **theme3, text='2')
num2.grid(row=5, column=1 )
num3 = tk.Button(calc_frame, **theme3, text='3')
num3.grid(row=5, column=2 )

minus_btn = tk.Button(calc_frame, **theme4, text='-')
minus_btn.grid(row=5, column=3 )



root.mainloop()