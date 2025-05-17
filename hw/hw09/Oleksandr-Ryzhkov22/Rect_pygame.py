import pygame

FPS = 60

WIDTH_DISPLAY=800
HEIGHT_DISPLAY=600

RECTANGLE = pygame.Rect(50, 50, 40, 60) 

WEIGHT = RECTANGLE.width
HEIGHT = RECTANGLE.height
COORD_X = RECTANGLE.x
COORD_Y = RECTANGLE.y
RECTANGLE_STEP=5

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
    
    if keys[pygame.K_LEFT]:
        COORD_X = COORD_X-RECTANGLE_STEP
    if keys[pygame.K_RIGHT]:
        COORD_X = COORD_X+RECTANGLE_STEP
    if keys[pygame.K_UP]:
        COORD_Y = COORD_Y-RECTANGLE_STEP
    if keys[pygame.K_DOWN]:
        COORD_Y = COORD_Y+RECTANGLE_STEP
        
    if COORD_X >= WIDTH_DISPLAY: 
        COORD_X = WIDTH_DISPLAY - RECTANGLE.width
    if COORD_Y >= HEIGHT_DISPLAY:
        COORD_Y = HEIGHT_DISPLAY - RECTANGLE.height
    
    if COORD_X < 0:
        COORD_X = 0
    if COORD_Y < 0:
        COORD_Y = 0 
              


    gameDisplay.fill(BLACK_COLOR) 

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X, 
                                              COORD_Y, 
                                              WEIGHT,
                                              HEIGHT])
    pygame.display.update()
    clock.tick(FPS)
    

