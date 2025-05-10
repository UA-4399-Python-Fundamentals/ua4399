# 1
even = []
odd = []
not_divisible = []
for number in range(1, 10):
    if number % 2 == 0:
        even.append(number)
    elif number % 3 == 0:
        odd.append(number)
    else:
        not_divisible.append(number)
print(even)
print(odd)
print(not_divisible)


# 2
login = input("Enter your login: ")
while str(login) == "First":
    print("Hello, my login friend")
    break
else:
    print("Error")
