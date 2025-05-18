# Task 1
int_list = [1, 2, 3, 4, 5]
float_list = []

for num in int_list:
    float_list.append(float(num))

print(float_list)

# Task 2
n = int(input("Enter a number: "))
a, b = 0, 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b
print("/n")

# Task 3
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")
