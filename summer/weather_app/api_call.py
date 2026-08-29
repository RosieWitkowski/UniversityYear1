import requests
import json 
from datetime import datetime, UTC

try:
    with open('assets/API_key.txt') as f:
        api_key = str(f.read().strip())
except:
    raise Exception("API key not found. Please go to https://openweathermap.org/api to generate one.")

url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}"

def get_data(city):
    data = requests.get(url.format(city, api_key))
    if not data:
        return None 
    data = data.json()
    save_log('data_dump.json', data)
    return data

def save_log(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_times(data):
    unix_date = data['dt']
    timezone = data['timezone']
    
    unix_date += timezone
    date = datetime.fromtimestamp(int(unix_date), UTC).strftime('%Y-%m-%d %H:%M:%S')
    date, time = date[:10], date[11:]
    
    sunrise, sunset = data['sys']['sunrise'] + timezone, data['sys']['sunset'] + timezone
    sunrise = datetime.fromtimestamp(int(sunrise), UTC).strftime("%H:%M")
    sunset = datetime.fromtimestamp(int(sunset), UTC).strftime("%H:%M")

    return sunrise, sunset, date, time 

def get_weather(data):
    KELVIN = 273.15 # For conversion kelvin to celcius
    data_group = data['main']
    temp, temp_feels, temp_min, temp_max = int(data_group['temp'] - KELVIN), int(data_group['feels_like'] - KELVIN), int(data_group['temp_min'] - KELVIN), int(data_group['temp_max'] - KELVIN)
    return data['weather'][0]['main'], temp, temp_feels, temp_min, temp_max


# Testing/example usage
data = get_data('London')
if not data: 
    raise Exception('Data not found') # In GUI, use status bar 
print("Weather", get_weather(data))
print("Times", get_times(data))