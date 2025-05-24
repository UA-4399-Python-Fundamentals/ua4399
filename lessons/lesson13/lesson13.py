# l = [i for i in range(10)]
# print(l)

# l = (i for i in range(10))
# print(l)
# l = range(10)
# print(l)

# l1 = [1,2,3,4,5]
# l2 = ["a", "b", "c", "d", "e"]
# print(zip(l1, l2))
# print(list(zip(l1, l2)))
# l3 = [1,2,3]
# print(list(zip(l1, l2, l3)))

# l = [1,2,3,4,5]
# l2 = map(lambda x: str(x**2), l)
# print(list(l2))

# s = "1,2,3,4"
# l2 = map(int, s.split(","))
# print(list(l2))

# from random import randint
# from functools import reduce

# # l = [randint(-100, 100) for i in range(20)]
# # print(l)
# # l2 = filter(lambda x: x > 0, l)
# # print(list(l2))

# l = [randint(1, 100) for i in range(10)]
# print(l)
# def my_add(x, y):
#     print(f"Adding {x} and {y}")
#     return x + y

# print(reduce(my_add, l))
# print(reduce(my_add, l, -100))
# N=10
# l = [ i for i in range(N)]
# g = (i for i in range(N))
# print(f"for N={N} l={l.__sizeof__()}\tl = {l}")
# print(f"for N={N} g={g.__sizeof__()} \tg= {g}")

# for i in range(1,5):
#     N=10**i
#     l = [ i for i in range(N)]
#     g = (i for i in range(N))
#     print(f"for N={N} l={l.__sizeof__()}")
#     print(f"for N={N} g={g.__sizeof__()}")

# print("l = ", l)
# print("g = ", g)
# for i in g:
#     print(i)

# l = [1,2,3,4,5]
# it = iter(l)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __iter__(self):
#         return iter((self.x, self.y))

#     def __next__(self):
#         return next(iter(self))
    

# p = Point(1, 2)
# print(p.__dict__)
# print(Point.__dict__)

# # print(Point.__sizeof__())


# class MyRenge:
#     def __init__(self, start, end=None, step=1):
#         if end is None:
#             end = start
#             start = 0
#         self.start = start
#         self.end = end
#         self.step = step

#     def __str__(self):
#         return f"MyRenge({self.start}, {self.end}, {self.step})"

#     def __iter__(self):
#         print(f"iter({self.start}, {self.end}, {self.step})")
#         return self

#     def __next__(self):
#         if self.start < self.end:
#             result = self.start
#             self.start += self.step
#             return result
#         else:
#             # raise StopIteration
#             return 10
        

# print(MyRenge(10))
# print(MyRenge(1, 10))
# print(MyRenge(-5, 10, 2))

# for i in MyRenge(-5, 10, 2):
#     print(i)


# def my_range(n):
#     print(f"my_range({n})")
#     current = 0

#     while current < n:
#         print(f"yield {current}")
#         yield current
#         print(f"after yield {current}")
#         current += 1

# print("-" * 20)
# m = my_range(10)
# print("-" * 20)

# print(m)
# print("-" * 20)
# print(next(m))
# print("-" * 20)
# print(next(m))
# print("-" * 20)
# print(next(m))
# print("-" * 20)
# print(next(m))
# print("-" * 20)
# print(next(m))
# print("-" * 20)
# print(next(m))
# print("-" * 20)
# print(next(m))
# print("-" * 20)
# print(next(m))
# print("-" * 20)
# print(next(m))
# print("-" * 20)
# print(next(m))
# print("-" * 20)
# print(next(m))
# print("-" * 20)

# for i in my_range(10):
#     print(i)

# def my_range(n):
#     print(f"my_range({n})")
#     for i in range(n):
#         print(f"yield {i}")
#         print(f"after yield {i}")
#     yield i
#     for i in "bvhdbvk":
#         print(f"yield {i}")
#         print(f"after yield {i}")
#     yield i
#     for i in [1,2,3,4,5, "a", "b", "c"]:
#         print(f"yield {i}")
#         print(f"after yield {i}")
#     return i

# m = my_range(3)
# for i in m:
#     input()
# print(i)

# def gen_random_text(n):
#     from random import choice
#     from string import ascii_letters, digits
#     with open("random.txt", "w") as f:
#         for _ in range(n):
#             text = ''.join(choice(ascii_letters + digits) for _ in range(10))
#             f.write(text + "\n")

# gen_random_text(1_000)

# def read_random_text():
#     with open("random.txt", "r") as f:
#         for line in f:
#             yield line.strip()


# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         result = func(*args, **kwargs)
#         print("*" * 30)
#         return result
#     return inner

# def minus(func):
#     def inner(*args, **kwargs):
#         print("-" * 30)
#         result = func(*args, **kwargs)
#         print("-" * 30)
#         return result
#     return inner

# @star
# @minus
# @star
# def add(x, y):
#     print(f"add({x}, {y})")
#     return x + y

# print(add(1, 2))

# # # add = star(add)
# # print(add(1, 2))
# import time
# def print_run_time(funk):
#     def wraper(*args, **kwargs):
#         start = time.time()
#         result = funk(*args, **kwargs)
#         end = time.time()
#         print(f"run func {funk.__name__} {args=} {kwargs=} {end - start}s")
#         return result
#     return wraper
# from random import randint
# @print_run_time
# def f(n=3):
#     r = randint(1, n)
#     print(f"sleep {r}s")
#     time.sleep(r)


# f(5)
# f(5)
# f(5)

# def symbol(_symbol, count=10):
#     def pr(func):
#         def inner(*args, **kwargs):
#             print(_symbol * count)
#             result = func(*args, **kwargs)
#             print(_symbol * count)
#             return result
#         return inner
#     return pr

# @symbol("*", 30)
# @symbol("<", 20)
# @symbol("+", 10)
# def add(a, b):
#     return a+b

# add(1, 5)
funks = {}

def params(*p):
    global funks
    def wraper(funk):
        funks[p] = funk
        def inner(*args):
            _p = tuple(type(element) for element in args)
            f = funks.get(_p)
            if f:
                return f(*args)
            else:
                print("error")
        return inner
    return wraper


@params(int, list)
def my_f(n, l):
    return [i + n for i in l]

@params(int, int)
def my_f(a, b):
    return a+b


print(my_f(10, [25, 35, 45]))
print(my_f(10, 20))

print(funks)
