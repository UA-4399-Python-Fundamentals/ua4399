import random
number = random.randint(1, 100)
for i in range(10):
    guess = int(input(f"Attempt {i+1}: Enter your guess: "))
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print("Congratulations! You guessed the number!")
        break
else:
    print(f"Sorry, you've used all 10 attempts. The number was {number}.")