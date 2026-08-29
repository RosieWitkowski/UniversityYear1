import tkinter as tk 
import api_call

# ~ WINDOW 
root = tk.Tk()
root.title("Weather App")
root.geometry("1200x700")
root.resizable(0,0)
root.config(bg='SkyBlue')

main_temp_var, temp_feel_var, temp_min_var, temp_max_var = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()

def search():
    output_label.config(text="Searching... ")
    query = search_bar.get()
    data = api_call.get_data(query)
    if not data:
        output_label.config(text="CITY NOT FOUND (or invalid API key)\nPlease check your search (or key) and try again.")
        return 
    output_label.config(text="CITY FOUND")
    root.after(3000, lambda: output_label.config(text=default_text))

    sunrise, sunset, date_adjusted, time =  api_call.get_times(data)
    sky_summary, main_temp, temp_feel, temp_min, temp_max = api_call.get_weather(data)

    main_temp_var.set(main_temp)
    temp_feel_var.set(temp_feel)
    temp_min_var.set(temp_min)
    temp_max_var.set(temp_max)

    date_label.config(text=f"📅DATE {date_adjusted}")
    city_label.config(text=f"🗺️CITY {query}")
    time_label.config(text=f"🕝TIME {time}")

    main_temp_label.config(text=f"Temperature: {main_temp}⁰C")
    min_temp_label.config(text=f"Low: {temp_min}⁰C")
    temp_feels_label.config(text=f"Feels like: {temp_feel}⁰C")
    max_temp_label.config(text=f"High: {temp_max}⁰C")

    sky_status_label.config(text=f"Sky: {sky_summary}")
    match sky_summary: 
        case 'Clouds':
            background.config(image=cloudy_sky)
        case'Rain' | 'Thunderstorm':
            background.config(image=rainy_sky)
        case 'Snow':
            background.config(image=snowy_sky)
        case _:
            background.config(image=default_sky)

    sunrise_label.config(text=f"☀️ Sunrise\n{sunrise}")
    sunset_label.config(text=f"🌙 Sunset\n{sunset}")

# Calls celcius to fahrenheit conversion and displays updated values
def convert_f():
    """main, min, feels, max = main_temp_label.cget('text'), min_temp_label.cget('text'), temp_feels_label.cget('text'), max_temp_label.cget('text')
    main, min, feels, max = get_nums(main)
    main_temp_label.config(text=f"Temperature: {main_temp}⁰C")
    min_temp_label.config(text=f"Low: {temp_min}⁰C")
    temp_feels_label.config(text=f"Feels like: {temp_feel}⁰C")
    max_temp_label.config(text=f"High: {temp_max}⁰C")"""
    if main_temp_var.get():
        main_temp, temp_min, temp_feel, temp_max = formula(main_temp_var.get(), temp_min_var.get(), temp_feel_var.get(), temp_max_var.get())

        main_temp_label.config(text=f"Temperature: {main_temp}⁰F")
        min_temp_label.config(text=f"Low: {temp_min}⁰F")
        temp_feels_label.config(text=f"Feels like: {temp_feel}⁰F")
        max_temp_label.config(text=f"High: {temp_max}⁰F")
    else:
        output_label.config(text="Please make a search before attempting to convert.")
        root.after(3000, lambda: output_label.config(text=default_text))

# Converts celcius to fahrenheit
def formula(main_temp, temp_min, temp_feel, temp_max):
    # (0°C × 9/5) + 32 
    return ((main_temp * 9/5) + 32), ((temp_min * 9/5) + 32), ((temp_feel * 9/5) + 32), ((temp_max * 9/5) + 32)

# ~ THEMES
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
widget_theme5 = {'fg': "#000000", 'bg': "#69B46C", **border2} 

# ~ CONTAINERS
main_frame = tk.Frame(root,width=1260, height=700)
main_frame.pack(fill='both', expand=True, padx=20, pady=20)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.columnconfigure(3, weight=1)
main_frame.columnconfigure(4, weight=1)

# ~ BACKGROUND 
default_sky = tk.PhotoImage(file="assets/default_sky.png")
cloudy_sky = tk.PhotoImage(file="assets/clouds2.png")
rainy_sky = tk.PhotoImage(file='assets/rain2.png')
snowy_sky = tk.PhotoImage(file='assets/snow.png')

background = tk.Label(main_frame, image=default_sky, **bg_theme)
background.place(x=0, y=0, relheight=1, relwidth=1)

# ~ WIDGETS
# ROW 0 - title and search bar
tk.Label(main_frame, text="Weather App ⛅", **font1, **widget_theme1).grid(row=0, column=0, padx=20, pady=20, sticky='nesw')

search_bar = tk.Entry(main_frame, **font1, **widget_theme1)
search_bar.grid(row=0, column=1, pady=20, sticky='nesw')
search_bar.insert(0,"Search your city")

search_bar.bind('<FocusIn>', lambda e: search_bar.delete(0, tk.END))
search_bar.bind('<Return>', lambda e: search())

submit_btn = tk.Button(main_frame, text="🔎", **widget_theme1, **font1, command=search) # Consider removing and just using keybinds to enter, auto refresh possible?
submit_btn.grid(row=0, column=2, pady=20, sticky='nesw')

# ROW 1 - city and time displays
date_label = tk.Label(main_frame, text="📅DATE / / ", **widget_theme3, **font3)
date_label.grid(row=1, column=0)

city_label = tk.Label(main_frame, text='🗺️CITY Use above searchbar', **widget_theme3, **font3)
city_label.grid(row=1, column=1)

time_label = tk.Label(main_frame, text="🕝TIME  :  ", **widget_theme3, **font3)
time_label.grid(row=1, column=2)

# ROW 2, 3, 4 - temperatures 
"""tk.Label(main_frame, text="(Next hour, celcius)", **widget_theme3, **font1).grid(row=2, column=2, pady=10)"""

main_temp_label = tk.Label(main_frame, text="Temperature: ⁰C", **widget_theme3, **font2)
main_temp_label.grid(row=3, column=0, columnspan=4, pady=10)

min_temp_label = tk.Label(main_frame, text="Min: ⁰C", **widget_theme3, **font1)
min_temp_label.grid(row=4, column=0, pady=10)

temp_feels_label = tk.Label(main_frame, text="Feels like: ⁰C", **widget_theme3, **font1)
temp_feels_label.grid(row=4, column=1, pady=10)

max_temp_label = tk.Label(main_frame, text="Max: ⁰C", **widget_theme3, **font1)
max_temp_label.grid(row=4, column=2, pady=10)

# ROW 5 - sky  
sky_status_label = tk.Label(main_frame, text="Sky: ", **widget_theme3, **font3)
sky_status_label.grid(row=5, column=1, pady=10)

# ROW 6 - sunrise and sunset times 
sunrise_label = tk.Label(main_frame, text="☀️ Sunrise\n", **widget_theme3, **font3)
sunrise_label.grid(row=6, column=0)

sunset_label = tk.Label(main_frame, text="🌙 Sunset\n", **widget_theme3, **font3)
sunset_label.grid(row=6, column=2)

# ROW 7 - Unit conversion 
tk.Button(main_frame, command=convert_f, text="PRESS TO convert to Fahrenheit -> ", **widget_theme5, **font1).grid(pady=20, row=7, column=1)
 
# Status bar 
default_text = "Use the search bar at the top of the screen to find your city! Please ensure you have a valid API key ready (see README.md for instructions)."
output_label = tk.Label(root, justify='center', wraplength=900,text=default_text, **widget_theme4, **font1)
output_label.pack(pady=5)

if __name__ == "__main__":
    root.mainloop()
