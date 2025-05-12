import pygame
import sys
from utils import game_logic

pygame.init()

clock = pygame.time.Clock()

# screen resolution and base settings
screen = pygame.display.set_mode((600,500))
screen_center = screen.get_width()//2
pygame.display.set_caption('Guess Number Game')

#color settings
orange_c = pygame.Color("Orange")
grey_c = (66, 66, 66)
white_c = (255, 255, 255)
turq_c = (27, 175, 184)

#base font settings
base_font = pygame.font.SysFont("Times", 18)
base_text_color = grey_c

# input settings
input_rect = pygame.Rect(screen_center-100, 100, 100, 40)
input_color_active = pygame.Color('Black')
input_color_inactive = pygame.Color('Grey')
input_color = input_color_inactive
#set input state
active = False

#main button settings
button_rect = pygame.Rect(input_rect.x+input_rect.width+10,100,100,40)
button_color = turq_c

#try again button settings
try_again_button_rect = pygame.Rect(screen_center-50,200,100,40)
try_again_button_color = pygame.Color("Orange")

#base game settings
intro_text = "Guess number between 0 and 100"
number_answer = game_logic.generate_number()
max_attempts = game_logic.GUESS_ATTEMPTS
current_attempts = 0
user_text = ''
messages = {
    "default":f"You have {max_attempts - current_attempts} attempts left",
    "success":"You won!",
    "final_error":"Wrong! You have no attempts left"
}
result_message = messages["default"]




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #if input clicked with mouse, change its color
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
                print(number_answer)
            else:
                active = False

            #if "check" button clicked, verify the result
            if button_rect.collidepoint(event.pos):
                if not user_text.isdigit():
                    result_message = "Please, enter a number"
                    pygame.display.flip()
                elif game_logic.check_answer(int(user_text), number_answer):
                    result_message = messages["success"]
                else:
                    current_attempts+=1
                    if current_attempts < max_attempts:
                        result_message=f"Your number is {game_logic.gt_or_less(number_answer,int(user_text))}. {messages["default"]}"
                        pygame.display.flip()
                    else:
                        result_message = messages["final_error"]
                    user_text = ''
            if try_again_button_rect.collidepoint(event.pos):
                print("try again")
                result_message = messages["default"]
                number_answer = game_logic.generate_number()
                current_attempts = 0
                user_text = ''
                pygame.display.flip()



        if event.type == pygame.KEYDOWN:
            #if deleted key pressed, delete last char
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                # if typed smth in the text input display it and save value
                user_text += event.unicode

    #set hover effects for buttons
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        button_color = turq_c
    else:
        button_color = grey_c
    if try_again_button_rect.collidepoint(pygame.mouse.get_pos()):
        try_again_button_color = pygame.Color("Orange")
    else:
        try_again_button_color = grey_c
    # set input color depends on mouse state
    if active:
        input_color = input_color_active
    else:
        input_color = input_color_inactive

        # set screen color
    screen.fill(white_c)

    #draw input rect
    pygame.draw.rect(screen, input_color, input_rect, 2, border_radius=5)
    input_text = base_font.render(user_text, True, base_text_color)
    #draw button rect
    pygame.draw.rect(screen,button_color,button_rect,20, border_radius=5)
    # set position for "check" text inside button
    button_text = base_font.render("Check", True, white_c)
    text_rect = button_text.get_rect(center=button_rect.center)
    #draw try again button
    pygame.draw.rect(screen,try_again_button_color,try_again_button_rect,width=20,border_radius=5)
    # set position for "Try again" text inside button
    try_again_button_text = base_font.render("Try again", True, white_c)
    try_again_text_rect = try_again_button_text.get_rect(center=try_again_button_rect.center)

    # render elements
    screen.blit(base_font.render(intro_text,True,base_text_color),(screen_center-120,20))
    screen.blit(input_text, (input_rect.x + 5, input_rect.y + 10))
    screen.blit(button_text, text_rect)
    screen.blit(base_font.render(result_message,True,base_text_color),(screen_center-100,150))
    screen.blit(try_again_button_text,try_again_text_rect)


    pygame.display.flip()


    clock.tick(60)
