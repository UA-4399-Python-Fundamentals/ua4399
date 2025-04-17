#Interchange the values of two variables without using the third variable
a = int(input("a: "))
b = int(input("b: "))
buf = a
a = b
b = buf
print('a =', a)
print('b =', b)