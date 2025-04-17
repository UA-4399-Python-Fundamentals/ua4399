#TASK 3
val1 = input("Enter first value")
val2 = input("Enter second value")

print (f"Your entered values: first = {val1}, second = {val2}")
val1, val2 = val2, val1
print(f"Values are swapped: first = {val1}, second = {val2}")
