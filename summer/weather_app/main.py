import tkinter as tk 
# import api_call

root = tk.Tk()
root.title("Weather App")
root.geometry("1200x700")
root.resizable(0,0)
root.config(bg='SkyBlue')

"""sunrise_theme = {'bg': "#F8AE64"}
day_theme = {'bg': "#9DC4DB"}
sunset_theme = {'bg': "#F3AACA"}
night_theme = {'bg': "#0F2031"}"""

# Themes
border1 = {'highlightbackground': 'black', 'highlightthickness': '4'}
border2 = {'highlightbackground': 'grey', 'highlightthickness': '2'}

font1 = {'font': ('Cascadia Code', 18, )}
font2 = {'font': ('Cascadia Code', 36, 'bold')}
font3 = {'font': ('Cascadia Code', 22, 'bold')}

bg_theme = {'fg': "#ffffff", **border1} 

widget_theme1 = {'fg': "#ffffff", 'bg': "#6BA7BD", **border2} 
widget_theme2 = {'fg': "#000000", 'bg': "#6BA7BD", **border2}
widget_theme3 = {'fg': "#000000", 'bg': "#ffffff"}
widget_theme4 = {'fg': "#000000", 'bg': "#6BA7BD", **border1} 

# Frames
main_frame = tk.Frame(root,width=1260, height=700)
main_frame.pack(fill='both', expand=True, padx=20, pady=20)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.columnconfigure(3, weight=1)
main_frame.columnconfigure(4, weight=1)


default_sky = tk.PhotoImage(file="assets/default_sky.png")
background = tk.Label(main_frame, image=default_sky, **bg_theme)
background.place(x=0, y=0, relheight=1, relwidth=1)

# IN ACTUAL CODE, GET SUNRISE/SUNSET FROM API_CALL
# time = api_call.get_time(14)
"""if time > 5:
    if time < 7:
        main_frame.config(**sunrise_theme)
    elif time < 20:
        main_frame.config(**day_theme)
    elif time < 21:
        main_frame.config(**sunset_theme)
    else:
        main_frame.config(**night_theme)
else:
    main_frame.config(**night_theme)"""

# ROW 0 - title and search bar
tk.Label(main_frame, text="Weather App ⛅", **font1, **widget_theme1).grid(row=0, column=0, padx=20, pady=20, sticky='nesw')

search_bar = tk.Entry(main_frame, **font1, **widget_theme1)
search_bar.grid(row=0, column=1, pady=20, sticky='nesw')
search_bar.insert(0,"Search your city")

submit_btn = tk.Button(main_frame, text="GO", **widget_theme1, **font1) # Consider removing and just using keybinds to enter, auto refresh possible?
submit_btn.grid(row=0, column=2, pady=20, sticky='nesw')

# ROW 1 - city and time displays
city = tk.Label(main_frame, text='🗺️CITY Use above searchbar', **widget_theme3, **font3)
city.grid(row=1, column=1)

time = tk.Label(main_frame, text="🕝TIME  :  ", **widget_theme3, **font3)
time.grid(row=1, column=2)

# ROW 2, 3, 4 - temperatures 
"""tk.Label(main_frame, text="(Next hour, celcius)", **widget_theme3, **font1).grid(row=2, column=2, pady=10)"""

temp_main = tk.Label(main_frame, text="Temperature: ⁰C", **widget_theme3, **font2)
temp_main.grid(row=3, column=0, columnspan=4, pady=10)

min_temp = tk.Label(main_frame, text="Min: ⁰C", **widget_theme3, **font1)
min_temp.grid(row=4, column=0, pady=10)

temp_feels = tk.Label(main_frame, text="Feels like: ⁰C", **widget_theme3, **font1)
temp_feels.grid(row=4, column=1, pady=10)

max_temp = tk.Label(main_frame, text="Max: ⁰C", **widget_theme3, **font1)
max_temp.grid(row=4, column=2, pady=10)

# ROW 5 - sky  
sky_status = tk.Label(main_frame, text="Sky: ", **widget_theme3, **font3)
sky_status.grid(row=5, column=1, pady=10)

# ROW 6 - sunrise and sunset times 
sunrise = tk.Label(main_frame, text="☀️ Sunrise \n ", **widget_theme3, **font3)
sunrise.grid(row=6, column=0)

sunset = tk.Label(main_frame, text="🌙 Sunset \n ", **widget_theme3, **font3)
sunset.grid(row=6, column=2)

# ROW 7 - output bar 
default_text = "Use the search bar at the top of the screen to find your city! Please ensure you have an API key ready (see README.md for instructions)."
output_label = tk.Label(root, justify='center', wraplength=900,text=default_text, **widget_theme4, **font1)
output_label.pack(pady=5)
root.mainloop()
