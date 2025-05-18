import pygame
import random
import sys

# Ініціалізація Pygame
pygame.init()
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT = pygame.font.SysFont(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вгадай число")

# Змінні гри
secret_number = random.randint(1, 100)
guess = ''
message = 'Вгадайте число від 1 до 100'
tries_left = 10
game_over = False

def draw_text(text, y, color=BLACK):
    rendered = FONT.render(text, True, color)
    rect = rendered.get_rect(center=(WIDTH // 2, y))
    screen.blit(rendered, rect)

def reset_game():
    global secret_number, guess, message, tries_left, game_over
    secret_number = random.randint(1, 100)
    guess = ''
    message = 'Вгадайте число від 1 до 100'
    tries_left = 10
    game_over = False

# Головний цикл гри
clock = pygame.time.Clock()
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if guess.isdigit():
                        num = int(guess)
                        if num < secret_number:
                            message = 'Занадто маленьке!'
                        elif num > secret_number:
                            message = 'Занадто велике!'
                        else:
                            message = f'Вітаємо! Ви вгадали число!'
                            game_over = True
                        tries_left -= 1
                        if tries_left == 0 and num != secret_number:
                            message = f'Ви програли. Було загадано: {secret_number}'
                            game_over = True
                        guess = ''
                elif event.key == pygame.K_BACKSPACE:
                    guess = guess[:-1]
                elif event.unicode.isdigit():
                    guess += event.unicode
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()

    draw_text("Гра: Вгадай число", 40)
    draw_text(f"Спроб залишилось: {tries_left}", 90)
    draw_text(message, 150)
    draw_text("Ваше число: " + guess, 200)

    if game_over:
        draw_text("Натисніть 'R' щоб зіграти ще раз", 300)

    pygame.display.flip()
    clock.tick(30)
