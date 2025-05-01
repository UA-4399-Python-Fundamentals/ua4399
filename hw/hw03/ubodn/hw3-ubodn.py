import math

# Task 1

PYTHONS_PHILOSOPHY = """
    1.Beautiful is better than ugly.
    2.Explicit is better than implicit.
    3.Simple is better than complex.
    4.Complex is better than complicated.
    5.Flat is better than nested.
    6.Sparse is better than dense.
    7.Readability counts.
    8.Special cases aren't special enough to break the rules.
    9.Although practicality beats purity.
    10.Errors should never pass silently.
    11.Unless explicitly silenced.
    12.In the face of ambiguity, refuse the temptation to guess.
    13.There should be one-- and preferably only one --obvious way to do it.
    14.Although that way may not be obvious at first unless you're Dutch.
    15.Now is better than never.
    16.Although never is often better than *right* now.
    17.If the implementation is hard to explain, it's a bad idea.
    18.If the implementation is easy to explain, it may be a good idea.
    19.Namespaces are one honking great idea -- let's do more of those!
    20.Beautiful is better than ugly.
    21.Explicit is better than implicit.
    22.Simple is better than complex.
    23.Complex is better than complicated.
    24.Flat is better than nested.
    25.Sparse is better than dense.
    26.Readability counts.
    27.Special cases aren't special enough to break the rules.
    28.Although practicality beats purity.
    29.Errors should never pass silently.
    30.Unless explicitly silenced.
    31.In the face of ambiguity, refuse the temptation to guess.
    32.There should be one-- and preferably only one --obvious way to do it.
    33.Although that way may not be obvious at first unless you're Dutch.
    34.Now is better than never.
    35.Although never is often better than *right* now.
    36.If the implementation is hard to explain, it's a bad idea.
    37.If the implementation is easy to explain, it may be a good idea.
    38.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
    39.Explicit is better than implicit.
    40.Simple is better than complex.
    41.Complex is better than complicated.
    42.Flat is better than nested.
    43.Sparse is better than dense.
    44.Readability counts.
    45.Special cases aren't special enough to break the rules.
    46.Although practicality beats purity.
    47.Errors should never pass silently.
    48.Unless explicitly silenced.
    49.In the face of ambiguity, refuse the temptation to guess.
    50.There should be one-- and preferably only one --obvious way to do it.
    51.Although that way may not be obvious at first unless you're Dutch.
    52.Now is better than never.
    53.Although never is often better than *right* now.
    54.If the implementation is hard to explain, it's a bad idea.
    55.If the implementation is easy to explain, it may be a good idea.
    56.Namespaces are one honking great idea -- let's do more of those!
    """

COUNT_WORD_BETTER = PYTHONS_PHILOSOPHY.count('better')
print(f"Word 'better' appears {COUNT_WORD_BETTER} times in text.")

COUNT_WORD_NEVER = PYTHONS_PHILOSOPHY.count('never')
print(f"Word 'never' appears {COUNT_WORD_NEVER} times in text.")

COUNT_WORD_IS = PYTHONS_PHILOSOPHY.count('is')
print(f"Word 'is' appears {COUNT_WORD_IS} times in text.")

TEXT_IN_UPPERCASE = PYTHONS_PHILOSOPHY.upper()
print(TEXT_IN_UPPERCASE)

REPLACE_I = PYTHONS_PHILOSOPHY.replace("i", "&")
print(REPLACE_I)


# Task 2

FOUR_DIGIT_NUMBER = int(input("Enter four-digit number: "))
NUMBER_TO_LIST = list(map(int, str(FOUR_DIGIT_NUMBER)))

# find product of digits
PRODUCT_OF_DIGITS = math.prod(NUMBER_TO_LIST)
print(f"Product of the digits of your number is {PRODUCT_OF_DIGITS}")

# number in reverse order
REVERSE_NUMBER = int(str(FOUR_DIGIT_NUMBER)[::-1])
print(f"Number in reverse order is {REVERSE_NUMBER}")

# number in ascending order
ASCENDING_NUMBER = int(''.join(map(str, sorted(NUMBER_TO_LIST))))
print(f"Number in ascending order is {ASCENDING_NUMBER}")


# Task 3

a = 5
b = 10

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

