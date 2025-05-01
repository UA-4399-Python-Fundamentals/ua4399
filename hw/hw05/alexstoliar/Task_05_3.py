# Get the number from the user
n = int(input("Enter a number: "))

# Start with 1 because factorial multiplies numbers
factorial = 1

# Calculate factorial
for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is {factorial}")