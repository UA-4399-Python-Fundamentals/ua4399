#Task 1
import pygame
import random
import sys
pygame.init()
s, f = pygame.display.set_mode((600, 200)), pygame.font.Font(None, 36)
n, i, m = random.randint(1, 100), '', 'Guess 1-100'
while 1:
    s.fill((255,255,255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT: sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                if i.isdigit():
                    x = int(i)
                    m = 'Correct!' if x == n else 'Low' if x < n else 'High'
                else: m = 'Numbers only'
                i = ''
            elif e.key == pygame.K_BACKSPACE: i = i[:-1]
            elif e.unicode.isdigit(): i += e.unicode
    s.blit(f.render("Guess: "+i, 1, (0,0,0)), (20, 50))
    s.blit(f.render(m, 1, (0,0,0)), (20, 100))
# Task 2
import pygame
FPS = 60
WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if WIDTH_DISPLAY < 500:
        WIDTH_RECTANGLE = 40
    if WIDTH_DISPLAY > 500:
        WIDTH_RECTANGLE = 40
    if HEIGHT_DISPLAY < 500:
        HEIGHT_RECTANGLE = 60
    if HEIGHT_DISPLAY > 500:
        HEIGHT_RECTANGLE = 60
    gameDisplay.fill(BLACK_COLOR)
    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
#Task 3
import requests
import tkinter as tk
from tkinter import *

def get_weather(city):
    api_key = "ef2206ff5da67de63306d0b143e20872"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"{data['name']}: {data['main']['temp']}°C, {data['weather'][0]['description']}"
    else:
        return "City not found."

def show_weather():
    city = entry.get()
    result = get_weather(city)
    label.config(text=result)
HEIGHT = 350
WIDTH = 450
root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
entry = tk.Entry(frame, font=('Courier', 12))
entry.place(relwidth=0.65, relheight=1)

btn = tk.Button(frame, text="Get Weather", font=('Courier', 12), command=show_weather)
btn.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="white", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()









