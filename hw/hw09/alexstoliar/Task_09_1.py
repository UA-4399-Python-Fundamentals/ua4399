import random

secret_number = random.randint(1, 100)
attempts = 0

while attempts < 10:
    user_input = input("Guess a number (1–100): ")
    try:
        guess = int(user_input)
    except ValueError:
        print("❌ That's not a number. Try again.")
        continue  # Skip this attempt and ask again

    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("🎉 Correct! You win!")
        break
else:
    print(f"😢 Out of attempts! The number was {secret_number}.")