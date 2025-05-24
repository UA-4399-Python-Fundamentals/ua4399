# In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

numbers = list(range(1, 11))
numbers_even, numbers_odd, numbers_other = [], [], []
for i in numbers:
    if i % 2 == 0:
        numbers_even.append(i)
    elif (i % 2 != 0) and (i % 3 == 0):
        numbers_odd.append(i)
    elif (i % 2 != 0) and (i % 3 != 0):
        numbers_other.append(i)

print(numbers_even)
print(numbers_odd)
print(numbers_other)
