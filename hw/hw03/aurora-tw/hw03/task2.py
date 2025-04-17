import math

GIVEN_NUM = 7284
NUMBERS_LIST = list(map(int, str(GIVEN_NUM)))

#TASK 2 Part 1
numbers_prod = math.prod(NUMBERS_LIST)
print(f"The product of digits in {GIVEN_NUM} = {numbers_prod}")


#TASK 2 Part 2
numbers_rev = NUMBERS_LIST.copy()
numbers_rev.reverse()
numbers_rev = int(''.join(map(str,numbers_rev)))
print(f"The reversed number {GIVEN_NUM} is: {numbers_rev}")

#TASK 2 Part 3
numbers_sorted = NUMBERS_LIST.copy()
numbers_sorted.append(GIVEN_NUM)
numbers_sorted.sort()

#convert assorted list to string for result
numbers_list_assorted = str(','.join(map(str,NUMBERS_LIST)))
#convert sorted list to string for result
numbers_sorted = str(','.join(map(str,numbers_sorted)))

print(f"The sorted list of digits {GIVEN_NUM},{numbers_list_assorted} is: {numbers_sorted}")

