import pygame
import random
import sys

pygame.init()

width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Guess the Number Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)

number_to_guess = random.randint(1, 100)
attempts = 10
user_input = ''
message = "Guess a number between 1 and 100"


def draw_text(text, y):
    rendered_text = font.render(text, True, BLACK)
    win.blit(rendered_text, (20, y))


running = True
while running:
    win.fill(WHITE)

    draw_text(f"Attempts left: {attempts}", 20)
    draw_text(message, 60)
    draw_text(f"Your input: {user_input}", 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_input.isdigit():
                    guess = int(user_input)
                    attempts -= 1
                    if guess < number_to_guess:
                        message = "Too low!"
                    elif guess > number_to_guess:
                        message = "Too high!"
                    else:
                        message = f"Correct! The number was {number_to_guess}"
                        attempts = 0
                else:
                    message = "Enter a valid number!"
                user_input = ''
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.unicode.isdigit():
                user_input += event.unicode

    if attempts == 0 and message != f"Correct! The number was {number_to_guess}":
        message = f"You lost! The number was {number_to_guess}"

    pygame.display.update()

pygame.quit()
sys.exit()