n=100
x, y = 1, 1
for i in range(n):
    print(x, end=' ')
    x, y = y, x + y
print()
