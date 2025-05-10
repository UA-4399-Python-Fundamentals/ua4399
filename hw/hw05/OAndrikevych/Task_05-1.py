# Task1. Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type.
print("Task 1\n")
a = int(input("Enter start value for integer list:"))
b = int(input("Enter stop value for integer list:"))
c = int(input("Enter step for integer list:"))
int_list = list(range(a, b, c))
print("\nInteger List:", int_list)

fl_list = []
for n in int_list:
    fl_list.append(float(n))
print("Float List:", fl_list)

# Task3. Write a script that will calculate the factorial of the entered number without using recursion.
print("\nTask 3\n")
def factorial(n):
    if n < 0:
        return "Negative numbers don't have a factorial"

    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

num = int(input("Enter a number to calculate the factorial: "))
print(f"Factorial of {num} = {factorial(num)}")

# Task2. Print Fibonacci numbers up to the entered number n, using cycles.
print("\nTask 2\n")
import matplotlib.pyplot as plt
import math

def fibonacci(n):
    fib_n = [0, 1]
    while fib_n[-1] + fib_n[-2] <= n:
        fib_n.append(fib_n[-1] + fib_n[-2])
    return fib_n

def alpha_fibonacci(n, alpha=(1 + math.sqrt(5)) / 2):
    alpha_n = [0, alpha]
    while alpha_n[-1] + alpha_n[-2] <= n:
        alpha_n.append(alpha_n[-1] + alpha_n[-2])
    return alpha_n

n = int(input("Enter max number for Fibonacci Sequence: "))

fib_seq = fibonacci(n)
alpha_fib_seq = alpha_fibonacci(n)

print("Fibonacci Sequence:", fib_seq)
print("α-Fibonacci Sequence:", [round(num, 3) for num in alpha_fib_seq])

# Plot
plt.plot(range(len(fib_seq)), fib_seq, marker="o", label="Fibonacci")
plt.plot(range(len(alpha_fib_seq)), alpha_fib_seq, marker="s", label="α-Fibonacci", linestyle="--")

plt.xlabel("Number in Sequence")
plt.ylabel("Fibonacci Value")
plt.title("Fibonacci vs α-Fibonacci Sequence")
plt.legend()
plt.grid()
plt.show()