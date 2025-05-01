#Calculate the factorial of a number without using recursion
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {n} is {factorial(n)}")
