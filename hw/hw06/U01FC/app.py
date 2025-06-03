# Task 1

RANGE = list(range(1, 11))
even_divisible_by_2 = []
odd_divisible_by_3 = []
not_divisible_by_2_or_3 = []
for num in RANGE:
    if num % 2 == 0:
        even_divisible_by_2.append(num)
    elif num % 3 == 0:
        odd_divisible_by_3.append(num)
    else:
        not_divisible_by_2_or_3.append(num)

print("Numbers divisible by 2:", even_divisible_by_2)
print("Numbers divisible by 3:", odd_divisible_by_3)
print("Numbers not divisible by 2 or 3:", not_divisible_by_2_or_3)

# Task 2

while True:
    login = input("Enter your login: ")
    if login == "First":
        print("Greetings")
        break
    else:
        print("Incorrect login, try again")
        