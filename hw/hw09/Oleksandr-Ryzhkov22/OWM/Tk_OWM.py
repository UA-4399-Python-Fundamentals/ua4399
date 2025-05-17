import tkinter as tk
from tkinter import font
from OWM import*
import pyowm

HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

get_weather = lambda owm: owm.weather_manager().weather_at_place(entry_field.get()).weather
def get_weather(owm):
    try:
        weather = owm.weather_manager().weather_at_place(entry_field.get()).weather
        label['text'] = f"Weather in {entry_field.get()}:\n" \
                        f"Status: {weather.detailed_status}\n" \
                        f"Temperature: {weather.temperature('celsius')['temp']}°C\n" \
                        f"Humidity: {weather.humidity}%\n" \
                        f"Wind Speed: {weather.wind()['speed']} m/s\n"
    except Exception as e:
        label['text'] = "Error: " + str(e)
    label['bg'] = 'gold'

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(owm))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
print (w.detailed_status)         # 'clouds'
print(w.wind())                  # {'speed': 4.6, 'deg': 330}
print(w.humidity)                # 87
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(w.rain)                    # {}
print(w.heat_index)              # None
print(w.clouds)      



label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

