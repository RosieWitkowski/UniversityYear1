import tkinter as tk 
import winsound

default_txt = 'Press duck to hear answer quacked!\nBig quack = number, Small quack = zero\nBig clock chime = end of number, Small chime = decimal point)'

def clear():
    output_display.config(text="")

def backspace():
    txt = str(output_display.cget('text'))
    output_display.config(text=txt[:-1]) 

def btn_press(char):
    output_display.config(text= str(output_display.cget("text")) + f'{char}')

def equals():
    output = output_display.cget('text')
    output_display.config(text="")
    output_display.config(text=eval(output))

def duck_btn():
    output = output_display.cget('text')
    num=""
    for char in str(output):
        if char in ['/', '*', '-', '+']:
            help_display.config(text=f"Cannot use duck button with non-numbers ({char})\nPlease use equals first or continue your calculation.")
            root.after(3000, lambda: help_display.config(text=default_txt))
            return 
        if char == '.':
            num = ""
            winsound.PlaySound(r'assets/small_chime.wav', winsound.SND_FILENAME)
            continue 
        try:
            num = int(char)
        except:
            output_display.config(text="Error") 
        if num == 0:
            winsound.PlaySound(r'assets/small_quack.wav', winsound.SND_FILENAME)
        else:
            for _ in range(num):
                winsound.PlaySound(r'assets/quack.wav', winsound.SND_FILENAME)
        num = ""
        winsound.PlaySound(r'assets/chime.wav', winsound.SND_FILENAME)

root = tk.Tk()
root.title("Quackulator")
root.geometry("720x680")

border = {'highlightbackground': 'black', 'highlightthickness': '1'}
theme1= {'bg': "#6167A3", 'fg': "#FFFFFF", 'font': ('Courier New', 28), **border}
theme2= {'bg': "#FF9319", 'fg': "#000000", 'font': ('Courier New', 18), **border}
theme3 = {'bg': "#B7B5FF", 'fg': "#000000", 'font': ('Courier New', 24), **border}
theme4 = {'bg': "#9E9DDD", 'fg': "#000000", 'font': ('Courier New', 24), **border}
theme5 = {'bg': "#DDE463", 'fg': "#000000", 'font': ('Courier New', 24), **border}
theme6 = {'bg': "#94FF19", 'fg': "#000000", 'font': ('Courier New', 12), **border}

calc_border = tk.Frame(root, height=600, width=450, )
calc_border.pack(pady=5)
calc_border.config(**border)

calc_frame = tk.Frame(calc_border)
calc_frame.pack(pady=15, padx=15)

# Output
output_display = tk.Label(calc_frame, text="", **theme1, width=15, anchor='w')
output_display.grid(row=0, column=0, columnspan=4)

# Clear and backspace
clear_btn = tk.Button(calc_frame, **theme2, text="C", command=clear)
clear_btn.grid(row=1, column=2)
back_btn = tk.Button(calc_frame, **theme2, text="<-X", command=backspace)
back_btn.grid(row=1, column=3, pady=10)

# Numbers and functions
# Row 0 (overall 3)
num1 = tk.Button(calc_frame, **theme3, text='7', command = lambda: btn_press(7))
num1.grid(row=3, column=0)
num8 = tk.Button(calc_frame, **theme3, text='8', command= lambda: btn_press(8))
num8.grid(row=3, column=1 )
num9 = tk.Button(calc_frame, **theme3, text='9', command= lambda: btn_press(9))
num9.grid(row=3, column=2 )

divide_btn = tk.Button(calc_frame, **theme4, text='/', command= lambda: btn_press('/'))
divide_btn.grid(row=3, column=3)

# Row 1 (overall 4)
num4 = tk.Button(calc_frame, **theme3, text='4', command= lambda: btn_press(4))
num4.grid(row=4, column=0 )
num5 = tk.Button(calc_frame, **theme3, text='5', command= lambda: btn_press(5))
num5.grid(row=4, column=1 )
num6 = tk.Button(calc_frame, **theme3, text='6', command= lambda: btn_press(6))
num6.grid(row=4, column=2 )

multiply_btn = tk.Button(calc_frame, **theme4, text='*', command= lambda: btn_press('*'))
multiply_btn.grid(row=4, column=3, pady=10)

# Row 2 (overall 5)
num1 = tk.Button(calc_frame, **theme3, text='1', command= lambda: btn_press(1))
num1.grid(row=5, column=0)
num2 = tk.Button(calc_frame, **theme3, text='2', command= lambda: btn_press(2))
num2.grid(row=5, column=1 )
num3 = tk.Button(calc_frame, **theme3, text='3', command= lambda: btn_press(3))
num3.grid(row=5, column=2 )

minus_btn = tk.Button(calc_frame, **theme4, text='-', command= lambda: btn_press('-'))
minus_btn.grid(row=5, column=3, pady=10)

# Row 3 (overall 6)
decimal_btn = tk.Button(calc_frame, **theme3, text='.', command = lambda: btn_press('.'))
decimal_btn.grid(row=6, column=0)
num0 = tk.Button(calc_frame, **theme3, text='0', command= lambda: btn_press(0))
num0.grid(row=6, column=1 )
root.update()
# print(num0.winfo_width(), num0.winfo_height())
euqals_btn = tk.Button(calc_frame, **theme4, text='=', command = equals)
euqals_btn.grid(row=6, column=2)
add_btn = tk.Button(calc_frame, **theme4, text='+', command= lambda: btn_press('+'))
add_btn.grid(row=6, column=3, pady=10 )

# Duck
duck_img = tk.PhotoImage(file=r'assets/duck_face.png')
duck_btn = tk.Button(calc_frame, **theme5, image=duck_img, command=duck_btn) 
duck_btn.grid(row=7, column=1, columnspan = 2)

# Help/status
help_display = tk.Label(calc_frame, **theme6,text=default_txt)
help_display.grid(row=8, column=0, columnspan=4)

root.mainloop()