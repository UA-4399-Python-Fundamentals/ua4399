#task 1
print("Task 1\n")
numbers_divisible_by_2 = []
numbers_divisible_by_3 = []
numbers_not_divisible_by_2_or_3 = []

for number in range(1, 11):
    if number % 2 == 0:
        numbers_divisible_by_2.append(number)
    elif number % 3 == 0:
        numbers_divisible_by_3.append(number)
    
    else:
        numbers_not_divisible_by_2_or_3.append(number)

print("Numbers divisible by 2:", numbers_divisible_by_2)
print("Numbers divisible by 3:", numbers_divisible_by_3)
print("Numbers not divisible by 2 or 3:", numbers_not_divisible_by_2_or_3)

#task 2
print("\nTask 2\n")
login = " "
while True:
    login = input("Enter your login: ")
    if login != "First":
        print("Incorrect login. Try again.\n")
        continue
    else:
        print("\nHello, First!\n")
        break