"""
Task 1: Create a list of integers and convert them to floats.
"""
my_list = [1, 2, 3, 4, 5]
print("Original list ", my_list)
my_list = [float(i) for i in my_list]
print("Generated list", my_list)

"""
Task 2. Create a Fibonacci sequence.
"""
n = input("Enter an integer to build Fibonacci list: ")
a, b = 0, 1
fib_sequence = []
while len(fib_sequence) < int(n):
    fib_sequence.append(a)
    a, b = b, a + b 
print(f"The Fibonacci list of {n} is {fib_sequence}")

"""
Task 3. Calculate the factorial of a number.
"""
m = input("Enter an integer to calculate its factorial: ")
factorial = 1 
for i in range(1, int(m) + 1):
    factorial *= i
print(f"The factorial of {m} is {factorial}")