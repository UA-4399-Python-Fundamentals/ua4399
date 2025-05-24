import random

guess_number = random.randint(1, 100)

ATTEMPTS = 10

print("Please guess a number between 1 and 100.")
print(f"You have {ATTEMPTS} attempts to guess it.")

for attempt in range(1, ATTEMPTS + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    if guess == guess_number:
        print(f"Congratulations! You guessed the number {guess_number} in {attempt} tries!")
        break
    if guess < guess_number:
        print("Too low!")
    else:
        print("Too high!")

    if attempt == ATTEMPTS:
        print(f"You've used all {ATTEMPTS} attempts. The correct number was {guess_number}.")
