number = 8692
product = 1
for digit in str(number):
    product *= int(digit)

reversed_number = int(str(number)[::-1])

sorted_number = int("".join(sorted(str(number))))

print(f"The product of the digits is: {product}")
print(f"Reversed number: {reversed_number}")
print(f"Sorted number (ascending): {sorted_number}")