# Task 1
print("Even numbers divisible by 2:")
for num in range(1, 11):
    if num % 2 == 0:
        print(num, end=" ")

print("\nOdd numbers divisible by 3:")
for num in range(1, 11):
    if num % 2 != 0 and num % 3 == 0:
        print(num, end=" ")

print("\nNumbers not divisible by 2 and 3:")
for num in range(1, 11):
    if num % 2 != 0 and num % 3 != 0:
        print(num, end=" ")
print("/n")

# Task 2
while True:
    login = input("Enter login: ")
    if login == "First":
        print("Hello, welcome!")
        break
    else:
        print("Error: Invalid login. Try again.")