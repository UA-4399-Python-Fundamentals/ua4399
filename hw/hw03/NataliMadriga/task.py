
#TASK 2
number = 57681;
s = str(number)
#product
print(int(s[0]) * int(s[1]) * int(s[2]) * int(s[3]) * int(s[4]))
#revers
print(int(s[::-1]))
#sort
print(''.join(sorted(str(number))))

#TASK 3
a = 5
b = 10
a, b = b, a
print(a)
print(b) 
