import random

def main():
    print("Try to guess the number 1-100\nYou have 10 attempts!")
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
        attempts += 1
        user_input = int(input("Your guess: "))
        if user_input < target_number:
            print("Your answer is smaller than target")
        elif user_input > target_number:
            print("Your answer is bigger than target")
        else:
            print(f"You have winned, the {user_input} is correct answer")
            return
    print(f"You loose! The correct number was {target_number}" )

if __name__ == "__main__":
    main()
        