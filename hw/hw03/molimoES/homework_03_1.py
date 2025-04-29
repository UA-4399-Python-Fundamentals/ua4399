# Homework Lesson 03

py_phil = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# ///////////////////////////////////////////////////////////////////
# 1 - Write Python's philosophy in the string format
print("Subtask 1")

# Number of occurrences of the words "better", "never" and "is"
occur_better = py_phil.count('better')
print(f"Number of word 'better': {occur_better}")
occur_never = py_phil.count('never')
print(f"Number of word 'never': {occur_never}")
occur_is = py_phil.count('is')
print(f"Number of word 'is': {occur_is}")

# Display all text in uppercase (all letters in uppercase)
print(py_phil.upper())

# Replace all occurrences of the symbol “i” with “&”
py_phil_repl = py_phil.replace('i', '&')
print(py_phil_repl)

# ///////////////////////////////////////////////////////////////////
# 2 - Operations with a four-digit natural number
print("Subtask 2")

four_digit_num = 4321
four_digit_str = str(four_digit_num)

# Find the product of the digits
product = int(four_digit_str[0]) * int(four_digit_str[1]) * int(four_digit_str[2]) * int(four_digit_str[3])
print(f"Product of the digits = {product}")

# Write the number in reverse order
four_digit_rev = four_digit_str[::-1]
print(f"Number in reverse order = {four_digit_rev}")

# Sort the numbers in ascending order
four_digit_lst = list(map(int, list(four_digit_str)))
print(f"Number in ascending order = {''.join(map(str, sorted(four_digit_lst)))}")

# ///////////////////////////////////////////////////////////////////
# 3 -Interchange the values of two variables without using the third variable
print("Subtask 3")

number_1 = input("Enter number 1: ")
number_2 = input("Enter number 2: ")

number_1, number_2 = number_2, number_1

print("Number 1 = ", number_1)
print("Number 2 = ", number_2)
