#======task 1=======
l = [1, 2, 3, 4, 5]
for index, i in enumerate(l):
    l[index] = float(l[index])
print(f"Float: {l}")

#======task 2======
n = int(input("Enter number: "))
previous = 0
current = 1
result = 0
fibo = [0]

if n == 0:
    print(fibo)
else:
    while result <= n:
        result = previous + current
        previous, current = current, result
        fibo.append(result)
    print(f"Fibonacci: {fibo}")

#======task 3======
n = int(input("Enter number: "))
factorial = 1
l = []
for i in range(n + 1):
    l.append(i)
for i in l:
    if i == 0:
        continue
    factorial *= i
print(f"Factorial: {factorial}")