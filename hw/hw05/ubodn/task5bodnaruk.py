# Task 1

INTEGER_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]

FLOAT_LIST = []

for num in INTEGER_LIST:
    FLOAT_LIST.append(float(num))

print(FLOAT_LIST)


# Task 2

n = int(input("Enter a number for fibonacci: "))

def fibonacci_up_to_n(n):
    a = 0
    b = 1
    
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

fibonacci_up_to_n(n)


# Task 3

x = int(input("Enter a non-negative integer to calculate its factorial: "))

def calculate_factorial(n):
    factorial = 1
    
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

print(calculate_factorial(x))
