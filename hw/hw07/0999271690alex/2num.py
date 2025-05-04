def max_of_two(a, b):
    return a if a > b else b

user_input = input("Enter two numbers separated by space: ")
a_str, b_str = user_input.split()
a = float(a_str)
b = float(b_str)

print("Max number is:", max_of_two(a, b))
