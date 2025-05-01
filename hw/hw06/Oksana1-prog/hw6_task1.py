#Task 1
numbers = range(1, 11)
even_divisible_by_2 = []
odd_divisible_by_3 = []
not_divisible_by_2_or_3 = []
for num in numbers:
    if num % 2 == 0:
        even_divisible_by_2.append(num)
    elif num % 3 == 0:
        odd_divisible_by_3.append(num)
    if num % 2 != 0 and num % 3 != 0:
        not_divisible_by_2_or_3.append(num)
print("Even numbers divisible by 2:", even_divisible_by_2)
print("Odd numbers divisible by 3:", odd_divisible_by_3)
print("Numbers not divisible by 2 and 3:", not_divisible_by_2_or_3)
#Task 2
while True:
    login = input("Enter your login: ")
    if login == "First":
        print("Hello, user!")
        break
    else:
        print("Error: Incorrect login. Please try again.")