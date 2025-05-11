# Homework Lesson 06

# ///////////////////////////////////////////////////////////////////
# 1 - Determine the range
print("Subtask 1")

even_nums = []
odd3_nums = []
no23_nums = []

for i in range(1,11):
    if i % 2 == 0:
        even_nums.append(i)
    elif i % 3 == 0:
        odd3_nums.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        no23_nums.append(i)

print(f"Even numbers that are divisible by 2: {even_nums}")
print(f"Odd numbers, which are divisible by 3: {odd3_nums}")
print(f"Numbers that are not divisible by 2 and 3: {no23_nums}")

# ///////////////////////////////////////////////////////////////////
# 2 - Check user login
print("Subtask 2")

while True:
    user_login = input("Enter your login: ")
    if user_login == "First":
        print("Congratulations!")
        break
    else:
        print("Incorrect input! Try again.")
