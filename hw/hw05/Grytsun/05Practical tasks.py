#Task 1 Convert integers in a list to floating-point numbers
int_list = [1, 2, 3, 4, 5]
float_list = []

for num in int_list:
    float_list.append(float(num))

print( float_list)

#Task 2 Generate Fibonacci numbers up to a given limit
number = int(input("Enter the limit: "))
a, b = 0, 1
print(end=" ")
while a <= number:
    print(a, end=" ")
    a, b = b, a + b 

#Task 3 Calculate the factorial of the entered number without recursion
n = int(input(" Enter a number to calculate its factorial: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")
