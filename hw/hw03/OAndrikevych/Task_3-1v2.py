# Task 03.1.1 v2
# Python's philosophy in the string format

pp = """
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
There should be one -- and preferably only one -- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# display all text in uppercase
print("Task 03.1.1\n")
pp = pp.upper()
print("The Zen of Python by Tim Peters in UPPERCASE\n", pp)

# number of occurrences of the words "better", "never" and "is"
better = f"Word 'better' occurrences\t= {pp.count('BETTER')}"
print(better)
never = f"Word 'never' occurrences\t= {pp.count('NEVER')}"
print(never)
w_is = f"Word 'is' occurrences\t\t= {pp.count('IS')}"
print(w_is)

# replace all occurrences of the symbol “i” with “&”
cor_i = pp.replace('I', '&')
cor_count = f"\nThere were {cor_i.count('&')} replacements of 'i' with '&'"
print(cor_count)

print("\nThe Zen of Python by Tim Peters after replacement of 'i' with '&'", cor_i)

# Task 03.1.2
# Manipulations with a four-digit natural number

print("Task 03.1.2\nManipulations with a four-digit natural number\n")

# Entering and verification number
def number():
    while True:
        nnnn = input("Enter 4-digit natural number: ")

        # Check for non-digit characters
        if not nnnn.isdigit():
            print("Invalid input. Please enter digits only.")
            continue

        # Check for exactly 4 digits
        if len(nnnn) < 4:
            nnnn = nnnn.zfill(4)
        elif len(nnnn) > 4:
            print("Invalid input. Please input exactly 4 digits.")
            continue

        print(f"\nThe number you inputed is:\t{nnnn}\n")

        dddd = [int(d) for d in nnnn]

        # find the product of the digits of this number
        prod = 1
        for d in dddd:
            prod *= d
        print(f"Product of number's digits:\t{prod}")

        # write the number in reverse order
        rev = nnnn[::-1]
        print(f"Number in reverse order:\t{rev}")

        # in ascending order, you need to sort the numbers included in the given number
        sort = ''.join(sorted(nnnn))
        print(f"Number in ascending order:\t{sort}")

        break
number()

# Task 03.1.3
# Interchange the values of two variables without using the third variable

print("Task 03.1.3\nInterchanging the values of two variables\n")

# Input a and b
a = input("Enter a: ")
b = input("Enter b: ")

print("\nBEFOR")
print("Variable a =", a)
print("Variable b =", b)

# Interchanging the values
a, b = b, a

print("\nAFTER")
print("Variable a =", a)
print("Variable b =", b)
print("END")