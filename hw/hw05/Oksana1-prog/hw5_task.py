#Task 1
int_list = [1, 2, 3, 4, 5]
for i in range(len(int_list)):
    int_list[i] = float(int_list[i])
print("List with float elements:", int_list)
#Task 2
n = int(input("Enter a number: "))
a, b = 0, 1
for _ in range(n):
    if a > n:
        break
    print(a, end=" ")
    a, b = b, a + b
#Task 3
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
    print(f"The factorial of {n} is {factorial}")