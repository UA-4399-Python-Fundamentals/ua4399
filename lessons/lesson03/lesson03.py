# b = True
# print(type(b), b)

# b = 10
# print(type(b), b)

# b = 10.1
# print(type(b), b)

# b = [10.1, "20.2", True]
# print(type(b), b)

# b = (10.1, "20.2", True)
# print(type(b), b)


# b = "10.1, 20xcvbds.2, 30.3"
# print(type(b), b)


# b = {1,2,3,1,2,3,1,2,3,1,2,3, "a", "b", "c", "b", "c"}
# print(type(b), b, len(b))
# f = 30

# l = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# b = {
#     "name": "John Doe",
#     "age": f,
#     11: False,
#     "courses": ["Math", "Science", "History"]
# }
# print(type(b), b)

# a = "Hello, World!"
# print(type(a), a, id(a))
# a = "Hello, Python!"
# print(type(a), a, id(a))
# a[1] = "a"  # This will raise an error because strings are immutable

# a = [1, 2, 3, 4, 5]
# print(type(a), a, id(a))
# a[1] = 10  # This will work because lists are mutable
# print(type(a), a, id(a))
# a.append(6)  # This will work because lists are mutable
# print(type(a), a, id(a))

# a = [1, 2, 3, 4, 5]
# print(type(a), a, id(a))
# print(type(a) is list)  # This will return True

# a = [1,2,3,4,5]
# b = a  # This will create a reference to the same list
# c = [1,2,3,4,5]
# print(a == b)  # This will return True because they have the same content
# print(a is b)  # This will return True because they are the same object in memory
# print(a == c)  # This will return True because they have the same content
# print(a is c)  # This will return False because they are different objects in memory
# print(id(a) == id(b))  # This will return True because they are the same object in memory

# a = [1,2,3,
#      4,
#      5]
# print(a)  # This will print the list with line breaks

# a = (
#     "Hello, World!"
#     "Hello, Python!"
#     "Hello, Java!"
#     "Hello, C++!"
# )
# print(a)  # This will print the concatenated string


# data = input("Enter is print: ")  # This will prompt the user for input
# if data == "print":
#  print("Hello, World!")
#  print("Hello, Python!")
#  if data == "print":
#     print("Hello, Java!")
#     print("Hello, C++!")


# print("End Hello, World!")


# def f():
#   a = 10


# a = 10
# print( a)
# a = 1_000_000_000
# print( a)

# a = 0b101010  # Binary representation of 42
# print( a)
# a = 0o52  # Octal representation of 42
# print( a)
# a = 0x2A  # Hexadecimal representation of 42
# print( a)

# class Person:pass
# a = Person()
# print( a)
# print(id(a))


# a = 10
# print(a, hex(a), oct(a), bin(a))

# for i in range(0, 50):
#     print(f"{bin(i)[2:]}\t{oct(i)[2:]}\t{i}\t{hex(i)[2:]}")


# f = 10.1
# print(f)
# f = 10.
# print(f)
# f = .1
# print(f)
# f = 123e4     
# print(f)
# f = 123e-2     
# print(f)


# b = True
# print(type(b), b)
# print(15 + b)
# b = False
# print(type(b), b)
# print(15 + b)

# b = None# nil, null, undefined, nul_ptr, none, none_type

# c = None
# print(b == c)
# print(b is c)

# a = [1,2,3,4,5]
# b = (6,7,8,9,10)
# a[1] = 10  # This will work because lists are mutable
# # b[1] = 20  # This will raise an error because tuples are immutable
# print(a[0])
# print(b[3])

# s = set("Hello, World!")
# print(s)
# print("l" in s)
# print("q" in s)
# f = "Hello, World!"
# d = {
#     "name": "John Doe",
#     "age": 30,
#     "is_student": False,
#     "courses": ["Math", "Science", "History"],
#     1: "one",
#     f: "two",
# }

# print(d)
# print(d["name"])
# print(d[1])
# print(d["Hello, World!"])
# d["name"] = "Liubomyr"
# print(d)
# c = d
# c = d.copy()
# from copy import deepcopy
# c = deepcopy(d)


# print(int(12.8))
# print(int(12.2))
# print(round(12.6))
# print(round(12.3))
# print(int("1010"))
# # print(int("1010aa"))  # This will raise an error because the string is not a valid integer
# print(int("1010", 2))

# s = str(15)
# print(s, type(s))
# s = "Hello, World!"
# l = list(s)
# print(l, type(l))
# l = tuple(s)
# print(l, type(l))
# l = set(s)
# print(l, type(l))
# l = dict(((1, "a"), (2, "b"), (3, "c")))
# print(l, type(l))
# print(list(enumerate(s)))

# for i in range(0, 256):
#     print(f"{i}\t{chr(i)}")


# for i in "range(0, 256)r":
#     print(f"{i}\t{ord(i)}")

# a = 'i\'m a string'
# print(a)

# s = "Hello, \rWo"
# print(s)

# template = """Hello, %s!
# Welcome to %s course.
# This is a %.5f year course.
# Enjoy your learning!
# """
# name = "Liubomyr"
# course = "Python"
# year = 2023

# print(template % (name, course, year))

# template = """Hello, {name}!
# Welcome to {course} course.
# This is a {year} year course.
# Enjoy your learning!
# """

# print(template.format(course=course, name=name,  year=year))


# print(f"Hello, {name}!\nWelcome to {course} course.\nThis is a {len(str(year**99))} year course.\nEnjoy your learning!")

text = "Hello, World!"
print(text[0])
print(text[-1])
print(text[0:5])
print(text[7:])
print(text[0:5])
print(text[::2])
print(text[::-1])
print(text[1:7:3])
print(text[40:50])
print(text[7:-7])
print(text[5:-5])