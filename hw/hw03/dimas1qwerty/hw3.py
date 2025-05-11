# === Task 1 ===
print("=== Task 1 ===")
text = """The Zen of Python, by Tim Peters: Beautiful is better than ugly. Explicit is better than implicit. 
Simple is better than complex. Complex is better than complicated. Flat is better than nested. 
Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. 
Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. 
In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. Now is better than never. 
Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"""

# Count occurrences
print("better:", text.count("better"))
print("never:", text.count("never"))
print("is:", text.count("is"))

# Display in uppercase
upper_text = text.upper()
print("\nUppercase Text:\n", upper_text)

# Replace 'i' with '&'
replaced_text = upper_text.replace('I', '&')
print("\nText with 'I' replaced:\n", replaced_text)

# === Task 2 ===
print("=== Task 2 ===")
number = 1234

# Product of digits
digits = [int(d) for d in str(number)]
product = 1
for d in digits:
    product *= d
print("Product of digits:", product)

# Reverse the number
reversed_number = int(str(number)[::-1])
print("Reversed number:", reversed_number)

# Sort digits in ascending order
sorted_digits = sorted(str(number))
print("Sorted digits:", ''.join(sorted_digits))

# === Task 3 ===
print("=== Task 3 ===")
a = 5
b = 10
print("Before swapping:")
print("a:", a)
print("b:", b)

a, b = b, a
print("After swapping:")
print("a:", a)
print("b:", b)
