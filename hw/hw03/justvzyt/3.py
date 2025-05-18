a = input("variable 1: ")
b = input("variable 2: ")

b = [a, b]
a = b[1]
b = b[0]
print(f"a = {a}, b = {b}")