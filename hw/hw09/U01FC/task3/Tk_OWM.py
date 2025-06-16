import tkinter as tk
from tkinter import font
import OWM

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


button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 8), justify='left', anchor='nw', wraplength=350)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

def get_weather():
    city = entry_field.get()
    w = OWM.get_weather(entry_field.get())
    status = w.detailed_status.capitalize()
    wind_speed = w.wind().get('speed', 'N/A')
    wind_deg = w.wind().get('deg', 'N/A')
    wind_gust = w.wind().get('gust', 'N/A') 
    wind_info = f"Wind: {wind_speed} m/s, {wind_deg}°, Gust: {wind_gust}"
    humidity = w.humidity
    temp_current = w.temperature('celsius').get('temp', 'N/A')
    temp_min = w.temperature('celsius').get('temp_min', 'N/A')
    temp_max = w.temperature('celsius').get('temp_max', 'N/A')
    temp_info = (f"Temperature: {temp_current}°C \n"
                 f"Min: {temp_min}°C, Max: {temp_max}°C")
    rain_info = w.rain
    heat_index = f"Heat Index: {w.heat_index}°C"
    clouds = w.clouds
    weather_display_text = (
        f"Weather in {city.capitalize()}:\n\n"
        f"Status: {status}\n"
        f"{wind_info}\n"
        f"Humidity: {humidity}%\n"
        f"{temp_info}\n"
        f"Rain: {rain_info}\n"
        f"{heat_index}\n"
        f"Clouds: {clouds}% cover"
    )
    label.config(text=weather_display_text) 

root.mainloop()

