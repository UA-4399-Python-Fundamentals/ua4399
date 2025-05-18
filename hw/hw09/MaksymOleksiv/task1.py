from random import randint
import pygame

pygame.init()
clock = pygame.time.Clock()

FPS = 15
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 30
GREEN = (0, 255, 0)
BlUE = (0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guess the Number")
font = pygame.font.Font(None, FONT_SIZE)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


button_color = pygame.Color('dodgerblue2')
button_hover_color = pygame.Color('lightskyblue3')
text_color = pygame.Color('white')
button_rect = pygame.Rect(100, 230, 200, 60)

def draw_button(surface, rect, text, hover=False):
    color = button_hover_color if hover else button_color
    pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(surface, pygame.Color('black'), rect, 2)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)


def win_check(in_text, attempt, num):
    g = int(in_text)
    attempt -= 1
    if g < number:
        return "Too low!"
    elif g > number:
        return "Too high!"
    else:
        return 0



number = randint(1, 100)
attempts = 10
guess = 0
input_text = ""
output_text = ""
prompt_text = ""
res = -1

game_over = False

while True:

    screen.fill(WHITE)

    draw_text("Guess a number between 1 and 100", font, BLACK, screen, 20, 20)
    draw_text("Attempts left: " + str(attempts), font, BLACK, screen, 20, 60)
    draw_text("Your guess: " + input_text, font, BLACK, screen, 20, 100)
    draw_text(output_text, font, BLACK, screen, 20, 140)
    draw_text(prompt_text, font, BLACK, screen, 20, 180)

    is_hover = button_rect.collidepoint(pygame.mouse.get_pos())
    draw_button(screen, button_rect, "Submit", is_hover)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    input_text += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text.isdigit():
                        res = win_check(input_text, attempts, number)
                        input_text = ""
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos) and input_text.isdigit():
                    res = win_check(input_text, attempts, number)
                    input_text = ""

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    number = randint(1, 100)
                    attempts = 10
                    input_text = ""
                    output_text = ""
                    prompt_text = ""
                    res = -1
                    game_over = False


    if res == 0:
        output_text = "You guessed it!"
        prompt_text = "(press SPACE to restart)"
        game_over = True
        res = -1
    elif isinstance(res, str):
        output_text = res
        attempts -= 1
        res = -1
        if attempts == 0:
            output_text = f"""Game Over! The number was {str(number)}"""
            prompt_text = "(press SPACE to restart)"
            game_over = True


    pygame.display.update()
    clock.tick(FPS)
