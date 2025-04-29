n = input("Enter a number")
fact = int(n)
result = 1
temp = []

for i in (range(1, fact + 1)):
    temp.append(str(i))
    result *= i
else:

    print(f"{n}! = " + " * ".join(temp) + f" = {result}")








