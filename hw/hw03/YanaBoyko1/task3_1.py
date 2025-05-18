#task 1
s = "Beautiful is better than ugly. \
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

better_count=s.count("better")
never_count=s.count("never")
is_count=s.count("is")

print(better_count)
print(never_count)
print(is_count)
print()

print("Uppercase text:")
print(s.upper())
print()

print("Text with 'i' replaced by '&':")
print(s.replace("i", "&"))

#task 2
n = 1099

print(int(str(n)[::-1]))

digits = str(n)                
product = int(digits[0]) * int(digits[1]) * int(digits[2]) * int(digits[3])
print(product)

print(sorted(digits))

#task 3
a = 5
b = 7
a, b = b, a

print(a)
print(b)



