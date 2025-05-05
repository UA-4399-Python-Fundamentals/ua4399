# Task 1 Determine numbers in the range from 1 to 10
for numbers in range(1, 11):
    if numbers % 2 == 0:
        print(f"{numbers} is even and divisible by 2")
    elif numbers % 2 != 0 and numbers % 3 == 0:
        print(f"{numbers} is odd and divisible by 3")
    else:
        print(f"{numbers} is not divisible by 2 or 3")


# Task 2 Check the login using a while loop
while True:
    login = input("Enter your login: ")
    if login == "First":
        print("Hello, user!")
        break
    else:
        print("Error: Invalid login. Try again.")