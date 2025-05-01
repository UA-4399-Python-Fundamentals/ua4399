number = input("four-digit number: ")

product = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
print(f"Product of digits: {product}")


print(f"Reverse order: {number[3]}{number[2]}{number[1]}{number[0]}")


nums = list(number)
nums.sort()
print(f"Sorted ascending: {nums}")