import tkinter as tk
from tkinter import font
from pyowm import OWM

# OWM
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Tkinter

HEIGHT = 350
WIDTH = 450

root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 10))
label.place(relx=0, rely=0, relwidth=1, relheight=1)
label["justify"] = "left"

# Adding OWM info

info = []
def get_weather(city):
    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(city)
    w = observation.weather

    info.append(w.detailed_status)         # 'clouds'
    info.append(w.wind())                  # {'speed': 4.6, 'deg': 330}
    info.append(w.humidity)                # 87
    info.append(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    info.append(w.rain)                    # {}
    info.append(w.heat_index)              # None
    info.append(w.clouds)                  # 75
    print(info)
    label["text"] = f"Detailed status: {info[0]}\nWind info:\n1. Speed: {info[1]["speed"]}\n2. Deg: {info[1]["deg"]}\n3. Gust: {info[1]["gust"]}\nHumidity: {info[2]}\nTemperature:\n1. Current: {info[3]["temp"]}\n2. Max: {info[3]["temp_max"]}\n3. Min: {info[3]["temp_min"]}\n4. Feels like: {info[3]["feels_like"]}\nClouds amount: {info[6]}"

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

root.mainloop()