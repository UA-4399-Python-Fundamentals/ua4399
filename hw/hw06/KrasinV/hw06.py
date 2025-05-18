###
# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

lst =[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
eo=[]
for i in lst:
    if i % 2 == 0:
        even.append(i)
    if i % 3 == 0:
        odd.append(i)
    if i % 2 != 0 and i % 3 != 0:
        eo.append(i)    
print(even)
print(odd) 
print(eo)

###
# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is different, send an error message.
# (need to use loop while)


login = list(input("Please enter Login:"))
secret = list("First")
i=0
if len(login) == len(secret):
    while i < (len(secret)) and login[i] == secret[i]:
        i = i+1
    if i == len(secret):
        print("Login Accepted")
    else:
        print("Error, Incorrect Login")
else:
    print("Error, Incorrect Login")
