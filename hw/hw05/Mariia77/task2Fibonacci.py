# Print Fibonacci numbers up to the entered number n, using cycles
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 ...
first = 0
second = 1
n = int(input("Enter a number: "))
while first <= n:
    print(first, end=' ')
    first, second = second, first + second
