# Task 1
r_lst = list(range(1, 11))

print("Even numbers that are divisible by 2:", [x for x in r_lst if not x % 2])

print("Odd numbers, which are divisible by 3:", [x for x in r_lst if not x % 3])

print("Numbers that are not divisible by 2 and 3:", [x for x in r_lst if x % 2 and x % 3])

# Task 2

while True:
    login = input("Enter your login: ")
    if login == "First":
        break
    print("Login is incorrect(try again)")

print("Login is correct!")
