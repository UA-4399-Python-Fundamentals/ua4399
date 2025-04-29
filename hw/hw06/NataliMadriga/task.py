#TASK1 
condition1 = [i for i in range(1, 11) if i % 2 == 0]
condition2 = [i for i in range(1, 11) if i % 2 != 0 and i % 3 == 0]
condition3 = [i for i in range(1, 11) if i % 2 != 0 and i % 3 != 0]
print(condition1)
print(condition2)
print(condition3)

#TASK2
while True:
    login = input("Enter your login: ")
    if login == "First":
        print("Welcome, First!")
        break
    else:
        print("Incorrect login, try again.")
