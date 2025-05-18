int_list = [1, 2, 3, 4, 5]
float_list = []

for num in int_list:
    float_list.append(float(num))

print(float_list)



n = int(input("Enter the limit: "))
a, b = 0, 1
while a <= n:
    print(a, end=' ')
    a, b = b, a + b



n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")
