#1
numbers = [1, 2, 3, 4, 5]

float_numbers = []

for number in numbers:
    float_numbers.append(float(number))
    
print(float_numbers)

#2
n = int(input("Введіть число n: "))

a, b = 0, 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b

#3

n = int(input("Введіть число для факторіалу: "))

factorial = 1

factorialRange = range(1, n + 1)

for i in factorialRange:
    sum = factorial * i
    factorial = sum

print("Факторіал:", factorial)
