import pygame
from colors import Colors
from pygame import Rect
from random import randint
import datetime

pygame.init()
font = pygame.font.SysFont("Calibri", 25, True, False)

gameDisplay = pygame.display.set_mode((800, 600))


pygame.display.set_caption("My first game")


clock = pygame.time.Clock()




done = False

FPS = 30
keys_down = {
    pygame.K_UP: False,
    pygame.K_DOWN: False,
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False,
}
tank_pos = (400, 300)
ball = (0, 0)
ball_speed = 20
ball_direction = (1, 1)  # Initial direction of the ball
ball_radius = 10
ball_color = Colors.RED
ball_rect = Rect(ball[0], ball[1], ball_radius * 2, ball_radius * 2)
ball_image = pygame.image.load("/Users/aurora/Desktop/py2025/ua4399/lessons/lesson09/ball.png")
# 

start_time = datetime.datetime.now()
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_UP:
                keys_down[pygame.K_UP] = True
            elif key == pygame.K_DOWN:
                keys_down[pygame.K_DOWN] = True
            elif key == pygame.K_LEFT:
                keys_down[pygame.K_LEFT] = True
            elif key == pygame.K_RIGHT:
                keys_down[pygame.K_RIGHT] = True
        elif event.type == pygame.KEYUP:
            key = event.key
            if key == pygame.K_UP:
                keys_down[pygame.K_UP] = False
            elif key == pygame.K_DOWN:
                keys_down[pygame.K_DOWN] = False
            elif key == pygame.K_LEFT:
                keys_down[pygame.K_LEFT] = False
            elif key == pygame.K_RIGHT:
                keys_down[pygame.K_RIGHT] = False

    ############################################################################
    gameDisplay.fill(Colors.WHITE)
    ball = (ball[0] + ball_speed * ball_direction[0] + ball_direction[0]*randint(0, ball_speed), ball[1] + ball_speed * ball_direction[1]+ ball_direction[1]*randint(0, ball_speed))
    print(ball)
    if ball[0] <= 0 or ball[0] >= 800:
        ball_direction = (-ball_direction[0], ball_direction[1])
    if ball[1] <= 0 or ball[1] >= 600:
        ball_direction = (ball_direction[0], -ball_direction[1])
    current_time = datetime.datetime.now()
    elapsed_time = (current_time - start_time).total_seconds()

    text = font.render(f"Elapsed time: {elapsed_time:.2f} seconds", True, Colors.BLACK)
    gameDisplay.blit(text, (10, 10))
    for key, pressed in keys_down.items():
        if pressed:
            if key == pygame.K_UP:
                tank_pos = (tank_pos[0], tank_pos[1] - 5)  
            elif key == pygame.K_DOWN:
                tank_pos = (tank_pos[0], tank_pos[1] + 5)
            elif key == pygame.K_LEFT:
                tank_pos = (tank_pos[0] - 5, tank_pos[1])
            elif key == pygame.K_RIGHT:
                tank_pos = (tank_pos[0] + 5, tank_pos[1])

    if tank_pos[0] < 0:
        tank_pos = (0, tank_pos[1])
    elif tank_pos[0] > 800 - 30:
        tank_pos = (800 - 30, tank_pos[1])
    if tank_pos[1] < 0:
        tank_pos = (tank_pos[0], 0)
    elif tank_pos[1] > 600 - 15:
        tank_pos = (tank_pos[0], 600 - 15)

   

    

 
    ball_rect = pygame.draw.circle(gameDisplay, ball_color, ball, ball_radius)
    gameDisplay.blit(ball_image, ball)
    pygame.draw.rect(gameDisplay, Colors.GRAY, Rect(tank_pos[0], tank_pos[1], 30, 15), width=0)   

    if ball[0] < tank_pos[0] + 30 and ball[0] > tank_pos[0] and ball[1] < tank_pos[1] + 15 and ball[1] > tank_pos[1]:
        break

    pygame.display.update()

    clock.tick(FPS)
