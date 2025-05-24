# Homework Lesson 09

# ///////////////////////////////////////////////////////////////////
# 1 - Random generates of a number
print("Subtask 1")

import random

rand_number = random.randint(1, 100)
for i in range(10):
    guess_number = int(input(f"Input the guess number from 1 to 100: "))
    if rand_number > guess_number:
        print("The random number is greater.")
    elif rand_number < guess_number:
        print("The random number is less!")
    else:
        print("Congratulations! You are a winner!")
        break
else:
    print("Attempts was expired... Try again.")
    