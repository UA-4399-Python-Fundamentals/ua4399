#======task 1======

even = []
odd = []
either = []
for i in range(1, 11):
    if i % 2 == 0:
        even.append(i)
    #checks for odd numbers that are divided by 3
    elif i % 3 == 0:
        odd.append(i)
    else:
        either.append(i)

print(f"{even}\n{odd}\n{either}")
#elif i % 2 != 0 and i % 3 != 0:
#       either.append(i)'''

#======task 2======

#just while loop
user = input("Username: ")
while user != "First":
    print("Error: Username is incorrect")
    user = input("Username: ")
print(f"Hello, {user}!")

#while loop and try-except
while True:
    user = input("Username: ")
    try:
        if user == "First":
            print(f"Hello, {user}!")
            break
        else:
            raise ValueError
    except ValueError:
        print("Error: Username is incorrect")
