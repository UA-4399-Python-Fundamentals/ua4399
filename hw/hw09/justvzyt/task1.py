import random

number = random.randint(1, 100)
for i in range(10):
    guess = int(input(f"Guess the number (1-100), try №{i+1}: "))
    if guess > number:
        print("The number that you chose is larger than the one that was generated!")
    elif guess < number:
        print("The number that you chose is lower than the one that was generated!")
    else:
        print("Congratulations!")
        break
else:
    print("======\nYou've used all 10 attemps.\n======")