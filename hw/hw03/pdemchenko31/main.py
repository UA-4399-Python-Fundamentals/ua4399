#Task1
print("--------TASK 1--------")
zen = "Simple is better than complex"

zen_clean = zen.lower()
zen_bet = zen_clean.count("better")
zen_nev = zen_clean.count("never")
zen_is = zen_clean.count("is")
print(f"{zen} \nAfter analyse we get the result\n Better: {zen_bet}\n Never: {zen_nev}\n Is: {zen_is}")

zen_up = zen.upper()
print(f"Zen in uppercase: {zen_up}")

zen_i = zen.replace("i", "&")
print(f"If we replace i with & we will get: {zen_i}")

#Task2
print("\n--------TASK 2--------")

number = 1387
print(f"Number is: {number}")
digits = [int(d) for d in str(number)]
product = 1
for d in digits:
    product *= d
print(f"Product of digits: {product}")

num_rev = int(str(number)[::-1])
print(f"Reversed number: {num_rev}")

asc_num = sorted(digits)
des_num = sorted(digits, reverse=True)
print(f"Ascending number line: {asc_num} \nDescending number line: {des_num}")

#Task3
print("\n--------TASK 3--------")
a = int(input("Enter any number: "))
b = int(input("Enter other number: "))

a, b = b, a
print(f"Look at this magic:\n 'a'= {a},\n 'b'= {b}")