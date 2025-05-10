number = int(input("Your number: "))

digits = [int(d) for d in str(number)]

product = 1
for d in digits:
    product *= d

reversed_number = int(str(number)[::-1])

sorted_number = sorted(digits)


print("Product of digits: ", product)
print("Reversed number: ", reversed_number)
print("Sorted number: ", sorted_number)
