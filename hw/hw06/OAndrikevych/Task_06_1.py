# Task 1
print("Task 1")
num = range(1, 11)
print("In range", list(num))

n_2, n_3, n_not = [], [], []

for n in num:
    if n % 2 == 0:
        n_2.append(n)
    elif n % 3 == 0:
        n_3.append(n)
    else:
        n_not.append(n)

print("Even numbers divisible by 2:", n_2)
print("Odd numbers divisible by 3:", n_3)
print("Numbers not divisible by 2 or 3:", n_not)

# Task 2
print("\nTask 2")
# Dictionary User:Login
user_logins = {
    "Oksana": "First",
    "Anna": "Second",
    "Guest": "123"
}

#with check for all logins in the directory
print("Option 1")
while True:
    log = input("Enter your login: ")

    for user, login in user_logins.items():
        if login == log:
            print(f"Hello, {user}!")
            break
    else:
        print("Error: Invalid login")
        continue
    break

# If the login is "First", then greet the users. If the login is different, send an error message
print("\nOption 2")
while True:
    log = input("Enter your login: ")

    if log == "First":
        print(f"Hello, {user}!")
        break
    else:
        print("Error: Invalid login")
        break