import pygame
from colors import Colors

pygame.init()
font = pygame.font.SysFont('Calibri', 25, True, False)

gameDisplay = pygame.display.set_mode((800,600))


pygame.display.set_caption('My first game')


clock = pygame.time.Clock()

WHITE = (255, 255, 255)


done = False

FPS = 30


keys = []

points = []

while not done:
# --- Main event loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN:
            print(f"User pressed a key.{event}")
            keys.append(event.key)
        elif event.type == pygame.KEYUP:
            print(f"User let go of a key. {event}")
            keys.remove(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
            print(event)
            points.append(event.pos)

############################################################################
    gameDisplay.fill(WHITE)


    
    if keys: print(f"Keys pressed: {keys}")

    for point in points:
            pygame.draw.circle(gameDisplay, Colors.RED, point, 5)
            text = font.render(f"{point[0]}, {point[1]}", True, Colors.BLACK)
            gameDisplay.blit(text, (point[0]-40, point[1] - 30))

    if len(points) > 2:
        pygame.draw.polygon(gameDisplay, Colors.FUCHSIA, points, 5)
    pygame.display.update()
    
    
    clock.tick(FPS)