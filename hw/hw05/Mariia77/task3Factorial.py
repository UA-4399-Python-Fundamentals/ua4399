# Write a script that will calculate the factorial of the entered number without using recursion.
# 0!=1, 1!=1, 2!=1*2, 3!= 1*2*3=6, ….
factorial = 1
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")
