#A four-digit natural number is specified:
#find the product of the digits of this number
#write the number in reverse order
#in ascending order, you need to sort the numbers included in the given number


n1 = int(input("Enter number: "))
b = n1 % 10
c = n1 % 100 // 10
d = n1 // 100 % 10
e = n1 // 1000
print(b * c * d * e)
data = [b, c, d, e]
print(sorted(data))
digit = n1 % 10
n2 = digit
n1 = n1 // 10
while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit
print('Reversed number:', n2)


