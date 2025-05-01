# a = (1,2,3)
# b, c, d = a 
# print(b, c, d) 


# a = 1,2
# print(a)
# # a, b = 1,2,3 #a, b = 1,2,3
# a, b, c = 1,2,3 #a, b = 1,2,3
# a=b=c=1
# c=1
# b=c
# a=b
# a,b,c = 3

# def printInfo():
#     print("foo")

# # printInfo()
# # printInfo()
# # printInfo()
# # printInfo()
# print(printInfo())

# def printInfo():
#     print("foo")
#     return "FOO"

# # printInfo()
# # printInfo()
# # printInfo()
# # printInfo()
# print(printInfo())
# print(printInfo)
# s = printInfo
# s()


# def printInfo():
#     print("foo")
#     return "FOO"
#     print("end")

# printInfo()

# def info():
#     """
#     print info
#     return: none
#     """
#     print("A")

# info()
# print(info.__doc__)
# help(info)

# print()

# def max(a, b):
#     if a > b:
#         return a
#     elif b > a:
#         return b
#     print("end f")

# print(f"{max(5, 2)=}")
# print(f"{max(5, 7)=}")
# print(f"{max(5, 7)=}")
# print(f"{max("aa", "b")=}")
# print(f"{max("aa", "A")=}")
# # print(f"{max("aa", 1)=}")#TypeError: '>' not supported between instances of 'str' and 'int'

# def printINT(n):
#     for i in range(n):
#         if i > 5:
#             return
#         print(i)

# printINT(9)


# # a>b?1:2
# 1 if a>b else 2


# def print_info(name, age, city):
#     print("="*10)
#     print(f"my name:{name}")
#     print(f"my age:{age}")
#     print(f"my city:{city}")
#     print("="*10)

# print_info("Liubomyr", 39, "Lviv")
# print_info("Oleh", 18, "IF")
# # print_info("Oleh", 18)#TypeError: print_info() missing 1 required positional argument: 'city'
# # print_info("Oleh")#TypeError: print_info() missing 2 required positional arguments: 'age' and 'city'
# # print_info("Oleh", 18, "IF", 11)#TypeError: print_info() takes 3 positional arguments but 4 were given

# name = 55

# def print_info(name, age, city):
#     print("="*10)
#     print(f"my name:{name}")
#     print(f"my age:{age}")
#     print(f"my city:{city}")
#     print("="*10)

# print_info

# def print_info(name, age=18, city="Lviv"):
#     print("="*10)
#     print(f"my name:{name}")
#     print(f"my age:{age}")
#     print(f"my city:{city}")
#     print("="*10)

# # print_info()#TypeError: print_info() missing 1 required positional argument: 'name'
# print_info("Liubomyr")
# print_info("Liubomyr2", 39)
# print_info("Liubomyr2", 39, "Busk")
# # print_info("Liubomyr2", 39, "Busk", 5) #TypeError: print_info() takes from 1 to 3 positional arguments but 4 were given

# def print_info(name="", age, city="Lviv"): #SyntaxError: parameter without a default follows parameter with a default
#     print("="*10)
#     print(f"my name:{name}")
#     print(f"my age:{age}")
#     print(f"my city:{city}")
#     print("="*10)

# def print_info(name, age=18, city="Lviv"):
#     print("="*10)
#     print(f"my name:{name}")
#     print(f"my age:{age}")
#     print(f"my city:{city}")
#     print("="*10)


# print_info("Liubomyr", 39, "Burshtyn")
# print_info("Liubomyr","Burshtyn", 39)
# print_info("Liubomyr",city="Burshtyn", age=39)
# print_info(name="Liubomyr",city="Burshtyn", age=39)
# # print_info(name="Liubomyr","Burshtyn", age=39)#SyntaxError: positional argument follows keyword argument

# # print("text", sep="*", end="->")

# def my_funk(a, b, *args, e=10, f=20, **kwargs):
#     print(f"{a=} {b=} {args=} {e=} {f=} {kwargs=}")


# my_funk(1,2)
# my_funk(1,2,3,4,5,6,7,8,9)
# my_funk(1,2,3,4,5,6,7,8,9,e=30,g=45,m=99)
# # my_funk(1,2,g=45,m=99, 3,4,5,6,7,8,9,e=30) #SyntaxError: positional argument follows keyword argument

# #error
# def my_funk(a, b,  e=10, f=20, *args, **kwargs):
#     print(f"{a=} {b=} {args=} {e=} {f=} {kwargs=}")

# # my_funk(1,2,3,4,5,6,7,8,9,e=30,g=45,m=99)
# my_funk(1,2,e=30,g=45,m=99)


# class temp():
#     def __del__(self): print(f"del: {id(self)}")

# CONST = "global"

# def my_funk(*args,**kwargs):
#     print(f"{args=}  {kwargs=}")

# my_funk(1,2,3,4,a=1,b=2, s=1)

# def f():
#     a = 10
#     b = temp()
#     print("f:", dir())

# print("g1:", dir())
# f()
# print("g2:", dir())
# # print(a) #NameError: name 'a' is not defined

# def f():
#     a = 10
#     b = temp()
#     print("f:", dir())
#     return b

# print("g1:", dir())
# c = f()
# print("g2:", dir())
# # print(a) #NameError: name 'a' is not defined




# CONST = "global"
# GLOBAL_LIST = []
# # def f():
# #     a = 10
#     print(CONST)
#     print("f:", dir())

# f()



# CONST = "global"
# def f():
#     a = 10
#     print(CONST)
#     GLOBAL_LIST.append("10")
#     GLOBAL_LIST = []
#     # CONST = 10
#     # print(CONST)
#     print("f:", dir())

# f()
# print(GLOBAL_LIST)


# CONST = "global"
# def f():
#     global CONST
#     a = 10
#     print(CONST)
#     CONST = 10
#     print(CONST)
#     print("f:", dir())

# f()
# print(CONST)

# def f(con):

#     print(CONST)
#     CONST = 10
#     print(CONST)
#     print("f:", dir())
# f(CONST)
# g = "global"
# def outer():
#     l = "local"
#     def inner():
#         l = "local__inner"
#         print(l, g)
#     inner()
#     print(l, g)

# print(outer())

# g = "global"
# def outer():
#     nonlocal g
#     l = "local"
#     def inner():
#         nonlocal l
#         l = "local__inner"
#         print(l, g)
#     inner()
#     g = 10
#     print(l, g)

# print(outer())



# def f1():
#     l = "f1"
#     def f2():
#         l = "f2"
#         def f3():
#             l="f3"
#             print(l)
#         f3()
#         print(l)
#     f2()
#     print(l)

# f1()

# def f1():
#     l = "f1"
#     def f2():
#         l = "f2"
#         def f3():
#             nonlocal l
#             l="f3"
#             print(l)
#         f3()
#         print(l)
#     f2()
#     print(l)

# f1()


# def print_i(start):
#     print(start)
#     print_i(start+1)


# def temp_recursion(max_recursion):
#     import sys
#     current = sys.getrecursionlimit()
#     sys.setrecursionlimit(max_recursion)
#     def dec(funk):
#         def inner(*a, **k):
#             r = funk(*a, **k)
#             return r
#         return inner
    
#     sys.setrecursionlimit(current)
#     return dec


# @temp_recursion(500)
# def print_i(start):
#     print(start)
#     print_i(start+1)

# print_i(10)

# def fibo(n):
#     if n < 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
    
# print(fibo(1))
# print(fibo(2))
# print(fibo(3))
# print(fibo(4))
# print(fibo(5))
# print(fibo(6))


# def sum(a, b):
#     return a+b
# print(sum(10, 20))

# sum = lambda a, b: a**2+b**2
# print(sum(10, 20))


# l = [1,2,3,4, "arbksd", 66, "aa"]
# print(l)

# def eq(obj):
#     if type(obj) in  [int, float]:
#         return obj
#     else:
#         return len(obj)

# l.sort(key=eq)
# print(l)

# l.sort(key= lambda obj: -obj if type(obj) in  [int, float] else -len(obj))
# print(l)