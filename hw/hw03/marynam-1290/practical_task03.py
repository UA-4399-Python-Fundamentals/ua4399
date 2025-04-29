# 1
message = "Complex is better than complicated"

print("Number of occurrences of the word better:", message.count("better"))
print("Number of occurrences of the word never:", message.count("never"))
print("Number of occurrences of the word is:", message.count("is"))
print(message.upper())
print(message.replace("i", "&"))


# 2
number = int(input("Enter your 4 digit number: "))
product = 1

while number > 0:
    digit = number % 10
    product = product * digit
    number = number // 10

print("This is the product of digits in your number: ", product)


number = int(input("Enter your 4 digit number: "))
reversed = str(number)[::-1]
print(reversed)


number = int(input("Enter your 4 digit number: "))
number = str(number)
print("".join(sorted(number)))


# 3
variable1 = "love"
variable2 = "hate"
print(f"I {variable1} you")

variable1, variable2 = variable2, variable1

print(f"I {variable1} you")
