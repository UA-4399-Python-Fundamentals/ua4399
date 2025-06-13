##task1
l = [1, 2, 3, 4, 5]
float_l = []
for i in l:
   float_l.append(float(i))
print(float_l)



##task2
def print_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

n = int(input("Enter a number: "))
print_fibonacci(n)

##task3
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is {factorial}")