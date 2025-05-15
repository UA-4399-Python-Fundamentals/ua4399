#task 1
zen = """Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!"""

# Count occurrences of each word
count_better = zen.split().count('better')
count_never = zen.split().count('never')
count_is = zen.split().count('is')

print(f"Occurrences of 'better': {count_better}")
print(f"Occurrences of 'never': {count_never}")
print(f"Occurrences of 'is': {count_is}")

# Display text in uppercase
print("\nText in uppercase:")
print(zen.upper())

# Replace 'i' with '&'
modified_zen = zen.replace('i', '&')
print(modified_zen)





#task 2

number = input("Enter a four-digit natural number: ")
if len(number) != 4 or not number.isdigit():
    print("Invalid input. Please enter a four-digit number.")
else:
    # Product of digits
    product = 1
    for digit in number:
        product *= int(digit)
    print(f"Product of digits: {product}")

    # Reverse the number
    reversed_num = int(number[::-1])
    print(f"Reversed number: {reversed_num}")

    # Sort digits in ascending order
    sorted_num = int(''.join(sorted(number)))
    print(f"Sorted digits: {sorted_num}")



#task 3
a = 5
b = 10
print(f"Before swap: a = {a}, b = {b}")
a = a + b
b = a - b
print(f"After swap: a = {a}, b = {b}")