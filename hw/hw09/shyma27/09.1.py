from random import randint

target = randint(1, 100)
attempt = 0
won = False
while attempt < 10:
    number = int(input("Enter a number: "))
    if number == target:
        print("You've won!")
        won = True
        break
    elif number > target:
        print("Target number is less.")
    else:
        print("Target number is greater.")
    attempt += 1

if not won:
    print("You've run out of tries :(")