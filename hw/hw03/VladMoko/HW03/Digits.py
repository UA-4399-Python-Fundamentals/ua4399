number = 9582

result = 1

for digit in str(number):
    result *= int(digit)
print(result)

number_revers = int(str(number)[::-1])
print(number_revers)

number_sort = int("".join(sorted(str(number))))

print(number_sort)

#Task №3

a = 5
b = 9

a = a + b
b = a - b
a = a - b