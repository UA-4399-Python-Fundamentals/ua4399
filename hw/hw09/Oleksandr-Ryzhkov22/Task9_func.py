import pygame
import random

def game_guess_number():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Guess the Number")
    screen.fill((0, 255, 255, 255))
    font = pygame.font.Font(None, 36)
    number_to_guess = random.randint(1, 100)
    attempts = 0
    count_guess = 0
    guessed = False

    while not guessed:
        for event in pygame.event.get(10):
            if event.type == pygame.QUIT:
                pygame.quit()
                return
    
        screen.fill((0, 255, 255, 255))
        text_surface = font.render("Guess a number between 1 and 100", True, (0, 0, 0))
        screen.blit(text_surface, (50, 50))

        guess = input("Enter your guess: ")
        if guess.isdigit():
            guess = int(guess)
            attempts += 1
            count_guess += 1
            if guess < 1 or guess > 100:
                feedback = "Please enter a number between 1 and 100."
            elif guess == number_to_guess:
                screen.fill((102, 205, 0, 255))
                feedback = f"Congratulations! You guessed it in {attempts} attempts."
                guessed = True
            elif guess < number_to_guess and count_guess < 10:
                screen.fill((0, 0, 255, 255))
                feedback = "Too low! Try again."
            elif guess > number_to_guess and count_guess < 10:
                screen.fill((255, 185, 15, 255))
                feedback = "Too high! Try again."
            elif count_guess >= 10:
                screen.fill((238, 59, 59, 255))
                feedback = f"You lose! {attempts} attempts. Try it again!"
                guessed = True
            
        else:
            feedback = "Please enter a valid number."

        feedback_surface = font.render(feedback, True, (0, 0, 0))
        screen.blit(feedback_surface, (50, 150))
        pygame.display.flip()

    pygame.time.wait(2000)
    pygame.quit()
    
