import random as r

#=========================================================================
#Part 1
print("=====Part 1=====")

zen = "Beautiful is better than ugly. \
Explicit is better than implicit. \
Simple is better than complex. \
Complex is better than complicated. \
Flat is better than nested. \
Sparse is better than dense. \
Readability counts. \
Special cases aren't special enough to break the rules. \
Although practicality beats purity. \
Errors should never pass silently. \
Unless explicitly silenced. \
In the face of ambiguity, refuse the temptation to guess. \
There should be one-- and preferably only one --obvious way to do it. \
Although that way may not be obvious at first unless you're Dutch. \
Now is better than never. \
Although never is often better than *right* now. \
If the implementation is hard to explain, it's a bad idea. \
If the implementation is easy to explain, it may be a good idea. \
Namespaces are one honking great idea -- let's do more of those!"

#words occurrences 
print(f"Number of 'better': {zen.count("better")}")
print(f"Number of 'never': {zen.count("never")}")
print(f"Number of 'is': {zen.count("is")}\n")

#uppercase
print(f"Upper Case:\n{zen.upper()}\n")

#replace chars
print(f"Replaced 'i' with '&':\n{zen.replace("i", "&")}\n")

#===============================================================
#Part 2
print("=====Part 2=====")

number = str(r.randint(1000, 9999))
print(f"Original: {number}")

#product of digits
result = 1
for i in number:
    result = int(i) * result
print(f"Product: {result}")

#reverse order
print(f"Reversed: {number[::-1]}")

#ascending order
sorted = sorted(number)
result = ""
for i in sorted:
    result = result + i
print(f"Ascending: {result}\n")

#==================================================================
#Part3
print("=====Part 3=====")

a = 1
b = [2]
print(a,b[0])

#swapping values
b.append(a)
a = b.pop(0)
b = b.pop(0)
print(a, b)
#print(a,b[0])