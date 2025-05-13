import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Guess the Number Game")

# Colors
Purple = (128, 0, 128)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 36)

# Game variables
number_to_guess = random.randint(1, 100)
attempts = 10
user_input = ''
message = "Guess a number between 1 and 100"

def draw_text(text, y):
    """Helper function to draw text on the screen."""
    rendered_text = font.render(text, True, BLACK)
    win.blit(rendered_text, (20, y))

# Game loop
running = True
while running:
    win.fill(Purple)

    # Display game information
    draw_text(f"Attempts left: {attempts}", 20)
    draw_text(message, 60)
    draw_text(f"Your input: {user_input}", 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Check if Enter is pressed
                try:
                    guess = int(user_input)
                    if guess < number_to_guess:
                        message = "Too low!"
                    elif guess > number_to_guess:
                        message = "Too high!"
                    else:
                        message = f"Congratulations! You guessed it: {number_to_guess}"
                        running = False
                    attempts -= 1
                    if attempts == 0 and guess != number_to_guess:
                        message = f"Game over! The number was {number_to_guess}"
                        running = False
                    user_input = ''
                except ValueError:
                    message = "Please enter a valid number!"
                    user_input = ''

            elif event.key == pygame.K_BACKSPACE:  # Handle backspace
                user_input = user_input[:-1]
            else:
                user_input += event.unicode  # Add typed character to input

    pygame.display.update()

pygame.quit()
sys.exit()