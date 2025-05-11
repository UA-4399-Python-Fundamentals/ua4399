import pygame
import random

pygame.init()

# Screen Options
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
BUTTON_COLOR = (100, 200, 100)
TEXT_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")

font = pygame.font.Font(None, 36)        # bold
small_font = pygame.font.Font(None, 28)  # normal

# Game Variables
my_num = random.randint(1, 100)
tries = 10
attempt = 1
user_guess = ""
attempts_list = []
game_over = False
message = "Guess my number (1-100)"
show_cursor = True

def draw_text(text, x, y, color, font_type=font):
    """ Displaying text on the screen """
    text_surface = font_type.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_button():
    """ 'Play again' button """
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 50, 200, 40)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    draw_text("Play again", WIDTH // 2 - 60, HEIGHT - 40, TEXT_COLOR)
    return button_rect

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_RETURN:
                if user_guess.isdigit():
                    num = int(user_guess)
                    attempts_list.append(f"{attempt}/10:   {num}")  # Add a try to the list
                    if num == my_num:
                        message = f"Congratulations! You win! The number is {my_num}!"
                        game_over = True
                    elif num < my_num:
                        message = "Your number is too low! Try a higher number!"
                    else:
                        message = "Your number is too high! Try a lower number!"

                    attempt += 1
                    user_guess = ""

                    if attempt > tries:
                        message = f"No more tries! My number was {my_num}."
                        game_over = True

            elif event.key == pygame.K_BACKSPACE:
                user_guess = user_guess[:-1]
            else:
                user_guess += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if draw_button().collidepoint(event.pos):
                my_num = random.randint(1, 100)
                attempt = 1
                user_guess = ""
                attempts_list.clear()  # Clear the list of attempts upon restart
                game_over = False
                message = "Guess a number (1-100)"

    # Header at top center of window
    title_surface = font.render("My first game. Guess the number", True, GREEN)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, 30))
    screen.blit(title_surface, title_rect)

    # game text
    if attempt <= tries:
        draw_text(f"Attempts: {attempt}/{tries}", 20, 50, BLACK)
    draw_text(message, 20, 80, BLACK)
    draw_text(user_guess, 20, 120, BLUE)

    # Blink cursor every 500ms
    if (pygame.time.get_ticks() // 500) % 2 == 0:
        show_cursor = True
    else:
        show_cursor = False

    # Text entered + blinking cursor
    draw_text(user_guess + ("|" if show_cursor else ""), 20, 120, GREEN)

    # Subtitle for the list of attempts
    draw_text("Your attempts:", 20, 160, BLACK)

    # Displaying a list of entered numbers
    y_offset = 190
    for attempt_text in attempts_list:
        draw_text(attempt_text, 20, y_offset, GRAY, small_font)
        y_offset += 30

    # "Play Again" button when game ends
    if game_over:
        draw_button()

    pygame.display.update()

pygame.quit()