import tkinter as tk
from tkinter import font
import requests

height = 500
width = 600

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
    except:
        final_str = "There is a problem retrieving the information."
    return final_str

def get_weather(city):
    weather_key = 'b39add481b5b9f4353d9507747e0a8ff'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

background_img = tk.PhotoImage(file='/Users/sisiwang/Code/python/checkWeather/backgroundpic-converted.png')
background_label = tk.Label(root, image=background_img)
background_label.place(relheight=1, relwidth=1)

frame = tk.Frame(root, bg='#80ccff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 16))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Check Weather', font=('Courier', 14), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80ccff', bd=6)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
