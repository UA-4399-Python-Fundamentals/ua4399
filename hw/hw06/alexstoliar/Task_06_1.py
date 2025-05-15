# Task 1
list1 = []
list2 = []
list3 = []
for number in range(1,11):
    if number % 2 == 0:
        list1.append(number)
    elif number % 2 != 0 and number % 3 == 0:
        list2.append(number)
    elif number % 2 != 0 and number % 3 != 0:
        list3.append(number)
        
print(f"Even and divisible by 2: {list1}")
print(f"Odd and divisible by 3: {list2}")
print(f"Numbers that are not divisible by 2 and 3: {list3}")

# Task 2
login = ""
while login != "First":
    login = input("Enter login: ")
    if login != "First":
        print("Wrong login.")
    else:
        print("The login is correct")