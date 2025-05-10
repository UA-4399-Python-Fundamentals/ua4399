#Print Fibonacci numbers up to a given number n.
n = int(input("Enter a number n: "))
a, b = 0, 1
while a <= n:
        print(a, end=' ')
        a, b = b, a + b