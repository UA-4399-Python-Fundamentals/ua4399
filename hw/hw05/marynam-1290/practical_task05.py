# 1
list_int = [2, 21, 47, 8]
for number in list_int:
    number = float(number)
    print(number)


# 2
n = 50
num1, num2 = 0, 1

while num1 <= n:
    print(num1)
    num1, num2 = num2, num1 + num2


# 3
entered_number = int(input("Enter your number: "))
num = 1
i = 1
while i <= entered_number:
    num *= i
    i += 1
print(num)
