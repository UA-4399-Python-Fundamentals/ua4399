# Homework Lesson 05

# ///////////////////////////////////////////////////////////////////
# 1 - Change list's elements
print("Subtask 1")

list = [1, 2, 3, 4, 5]
list = [float(num) for num in list]

print(list)

# ///////////////////////////////////////////////////////////////////
# 2 - Fibonacci numbers
print("Subtask 2")

number = int(input("Enter the number to create Fibonacci numbers: "))

prev_num, next_num = 0, 1
print(prev_num, end = " ")

while next_num <= number:
    print(next_num, end = " ")
    prev_num, next_num = next_num, prev_num + next_num

# ///////////////////////////////////////////////////////////////////
# 3 - Calculate the factorial
print("Subtask 3")

number = int(input("Enter the number to calculate factorial: "))
fact_res = 1
fact_str = ""

for i in range(1, number + 1):
    fact_res *= i
    fact_str = "1" if fact_str == "" else fact_str + "*" + str(i)

print(f"{number}! = {fact_str} = {fact_res}")
