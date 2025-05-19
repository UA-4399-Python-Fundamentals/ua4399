import random

secret_number = random.randint(1, 100)

max_attempts = 10

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}/{max_attempts}. Guess the number (1–100): "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempt} tries.")
        break
else:
    print(f"Sorry, you've used all {max_attempts} tries. The number was {secret_number}.")
