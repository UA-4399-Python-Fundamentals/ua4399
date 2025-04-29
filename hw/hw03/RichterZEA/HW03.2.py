number = input("Enter a four-digit natural number: ")

# Product of numbers
result = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
print("product of the digits of this number:", result)

# Reverse order
reversed_number = number[::-1]
print("Number is reverse order:", reversed_number)

# Ascending order
sorted_number = "".join(sorted(number))
print("Numbers in ascending order:", sorted_number)