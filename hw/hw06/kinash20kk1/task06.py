##task1
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

##task2
login = ""
while login != "First":
    login = input("Enter login: ")
    if login != "First":
        print("Wrong login.")
    else:
        print("The login is correct")