#task1
from sympy.codegen.ast import continue_

philosophy = "I have never seen a place that is so beautiful. It's better for me i, int, i"
print('Number of occurrence of better:', philosophy.count('better'))
print('Number of occurrence of never:', philosophy.count('never'))
print('Number of occurrence of is:', philosophy.count('is'))
print('UPPER STRING',philosophy.upper())
print('replace string',philosophy.replace("i","&"))

#task2
#find the product of the digits of this number
#result = 1
#for i in str(number):
#    result *= int(i)
#print(result)

number = 2134
result = int(str(number)[0]) * int(str(number)[1]) * int(str(number)[2]) * int(str(number)[3])
print(result)


#write the number in reverse order
print(str(number)[::-1])

#in ascending order, you need to sort the numbers included in the given number
print(sorted(str(number)))

#task3
#Interchange the values of two variables without using the third variable.
var1 = "Hello"
var2 = "World"

var1, var2 = var2, var1
print(var1)
print(var2)


for i in range(101):
    if i % 2 == 0:
        print(i)

for i in range(101):
    if i % 2 == 0:
        continue
    print(i)

list = [1,2,3,4,5]
for i in  list:
    if i % 2 == 0:
        break
    print(i)



