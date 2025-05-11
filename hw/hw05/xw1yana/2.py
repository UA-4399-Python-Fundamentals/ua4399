number = int(input("Введіть число: "))

a, b = 0, 1
print(a, end = " ")
while b <= number:
    print(b, end = " ")
    a, b = b, a + b