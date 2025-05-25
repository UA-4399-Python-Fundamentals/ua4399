import random 

attempts = 0
target_number = random.randint(1, 100)


while attempts < 10:
    guess_number = int(input("Enter number: "))
    attempts += 1
    if target_number == guess_number:
        print("Congratulations! You guessed it!")
        break
    elif guess_number < target_number:
        print("Too small")
    else:
        print('Too big')
else:
    print(f"The attempts are over!")


print(f"The number was: {target_number}")
print(f"Attempts spent: {attempts}")