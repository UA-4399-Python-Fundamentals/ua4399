n = int(input("Enter the limit: "))

first = 0
second = 1

while first <= n:
    print(first, end=' ')
    first, second = second, first + second

print()
