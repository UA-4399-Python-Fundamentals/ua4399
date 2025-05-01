number = 1234
# Find the product of the digits of the number
product = 1
for digit in str(number):
    product *= int(digit)
# Write the number in reverse order
reversed_number = str(number)[::-1]
# Sort the numbers in ascending order
sorted_number = ''.join(sorted(str(number)))
print("Product of digits:", product)
print("Reversed number:", reversed_number)
print("Sorted digits:", sorted_number)

