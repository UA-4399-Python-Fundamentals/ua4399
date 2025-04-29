num = input("Enter a number: ")

print("Product of digits:", int(num[0]) * int(num[1]) * int(num[2]) * int(num[3]))

print("Reverse order:", num[3], num[2], num[1], num[0])

nums = list(num)
nums.sort()
print("Sorted ascending:", ', '.join(nums))