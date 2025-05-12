''' Home work 03 task1.2'''
"Task"
# A four-digit natural number is specified:
# - find the product of the digits of this number
# - write the number in reverse order
# - in ascending order, you need to sort the numbers included in the given number

"Declared variables"
valid_number = None

"input validation"
while valid_number is None:
    four_digit_number = input("please enter four digit natural number: ")
    if four_digit_number.isdigit() and len(four_digit_number)/4 == 1 and '.' not in four_digit_number \
        and ',' not in four_digit_number:
        valid_number = str(four_digit_number)
    else:
        print("Invalid input. Please enter a four digit natural number.")

"Output of the task result"
print(f"product of the digits of number {valid_number}:\
      {int(valid_number[0])*int(valid_number[1])*int(valid_number[2])*int(valid_number[3])}")
print(f"number {valid_number} in reverse order: {valid_number[::-1]}")
print(f"sorted numbers included in the number {valid_number}: {''.join(sorted(valid_number))}")