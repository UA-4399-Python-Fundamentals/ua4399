def print_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

# Get the number from the user
n = int(input("Enter a number: "))
print_fibonacci(n)