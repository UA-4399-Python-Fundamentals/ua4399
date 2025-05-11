####HW05
# Task1. Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type.
# (Hint: use the built-in float () function).
# Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)
# Task3. Write a script that will calculate the factorial of the entered number without using recursion.
# Example: 0!=1, 1!=1, 2!=2, 3!= 1*2*3=6, ....

#Task1:
list = [1, 2, 3, 4, 5]
float_list=[]
for i in list:
    float_list.append(float(i))
print(list)
print(float_list)

#Task2:
input = int(input("Enter number :"))
a = 0
b = 1
i = 0
for i in range(input):
    a, b = b, a + b
    i=i
    print (i,"=", a)

#Task3:
n = int(input("Enter number :"))
string=""
result = 1
if n == 0:
    print(f"{n}!=1")
elif n==1:
    print(f"{n}!=1")
elif n<0:
    print(f"{n}!=Wrong Number")
elif n > 1:
    for i in range(1,n+1):
        result = result * i 
        string = string + ("*"+str(i))
    print(f"{n}!={string[1:]}={result}")