import tkinter as tk
from tkinter import font
from pyowm import OWM
from pyowm.utils.config import get_default_config

# OpenWeatherMap API key
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Function to get weather based on city input
def get_weather():
    city = entry_field.get()
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        description = w.detailed_status
        temperature = w.temperature('celsius')['temp']
        humidity = w.humidity
        wind = w.wind()['speed']

        result = (
            f"Weather in {city}:\n"
            f"Condition: {description}\n"
            f"Temperature: {temperature} °C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} m/s"
        )
    except Exception as e:
        result = f"Error: {str(e)}"

    label.config(text=result)

# GUI setup
HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(
    frame, text="Get Weather", bg="gray", fg="white",
    font=('Courier', 8), command=get_weather
)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12), justify='left', anchor='nw')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()