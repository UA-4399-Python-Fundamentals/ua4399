import tkinter as tk
from tkinter import font
from OWM import get_weather

def display():
    '''Gets weather details from module OWM, add them into string and draws on Label'''
    w = get_weather(entry_field.get())
    result = f"General: {w.detailed_status}\nWind: {w.wind().get("speed")}\nHumidity: {w.humidity}\nTemp: {w.temperature('celsius').get("temp")}\nRain: {w.rain.get("1h")}\nHeat index: {w.heat_index}\nClouds: {w.clouds}"
    label.config(text=result)


HEIGHT = 550
WIDTH = 750


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
                   command=display)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()

