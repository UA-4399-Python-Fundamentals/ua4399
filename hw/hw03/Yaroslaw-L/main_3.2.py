import random
four_digit = str(random.randint(1000, 9999))
print(four_digit)
#3.2.1
product = int(four_digit[0])*int(four_digit[1])*int(four_digit[2])*int(four_digit[3])
print(f"Product: {product}")
#3.2.2
print(f"Reverse order: {four_digit[::-1]}")
#3.2.2
asc_order = sorted(four_digit)
print(f"Ascending order: {''.join(asc_order)} ")
