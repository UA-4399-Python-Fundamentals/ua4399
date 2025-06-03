# Task 1

integer_list = [1, 24, 3, 4, 52, 6, 75, 8, 96, 10]
integer_list = [float(i) for i in integer_list ]
print("Converted list:", integer_list)

# Task 2

end_value = int(input("End: "))
iteration = 0
fibonacci_sequence = []
while True:
    if iteration == 0:
        fibonacci_sequence.append(0)
        iteration += 1
    elif iteration == 1:
        fibonacci_sequence.append(1)
        iteration += 1
    else:
        temp = fibonacci_sequence[iteration - 1] + fibonacci_sequence[iteration - 2]
        if temp >= end_value:
            break
        fibonacci_sequence.append(temp)
        iteration += 1


print("Fibonacci sequence:", fibonacci_sequence)

# Task 3

input_number = int(input("Enter a number: "))
factorial = 0
for i in range(input_number):
    if i == 0 or i == 1:
        factorial = 1
    else:
        factorial *= i
print(f"Factorial of {input_number} is: {factorial}")