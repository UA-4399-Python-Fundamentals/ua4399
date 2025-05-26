import tkinter as tk
from tkinter import font
from pyowm import OWM

from PIL import Image, ImageTk
import requests
from io import BytesIO

owm = OWM('ef2206ff5da67de63306d0b143e20872')

#Start here
mgr = owm.weather_manager()
def get_weather():
    city = entry_field.get()
    observation = mgr.weather_at_place(city)
    w = observation.weather        
    ds = w.detailed_status         # 'clouds'
    wnd = w.wind()                  # {'speed': 4.6, 'deg': 330}
    hmd = w.humidity                # 87
    tc = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    rain = w.rain                    # {}
    heat = w.heat_index              # None
    cld = w.clouds                  # 75
    ico = w.weather_icon_name
    icon_url = f"http://openweathermap.org/img/wn/{ico}.png"
    response = requests.get(icon_url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    photo = ImageTk.PhotoImage(img)
    icon_label.config(image=photo)
    icon_label.image = photo    
    result = (f"In {city}: {ds}\n"
              f"Wind: {wnd['speed']}\n"
              f"Humidity: {hmd}\n"
              f"Temperature, ℃: {tc['temp']}\n"
              f"It's rainy? {rain}\n"
              f"It's heaty? {heat}\n"
              f"It's cloudy? {cld}"
              )
    label.config(text = result + "\n")
#end

HEIGHT = 450
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


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

#ico
icon_label = tk.Label(lower_frame, bg='gold')
icon_label.place(relx=0.5, rely=0.77, anchor='n')
#ico_end

root.mainloop()