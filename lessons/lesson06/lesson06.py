# list

# l = list()
# print(type(l), l)


# # l = list(123) #TypeError: 'int' object is not iterable
# l = list("hello")
# print(type(l), l)
# l = list(set("hello"))
# print(type(l), l)
# l = []
# print(type(l), l)
# l = list(("hello", 1, 2.0, True))
# print(type(l), l)
# l = ["hello", 1, 2.0, True]
# print(type(l), l)
# l = list(list(("hello", 1, 2.0, True)))
# print(type(l), l)
# l= [1, 2, 3, 4, 5, [1,2,3,4], list("hello"), list((1,2,3)), [1,2,3], list]
# print(type(l), l)
# print(l[-1]("foo"))
# l[0] = 100
# print(l, l[0])
# print(l[-1], l[-2])
# print(l[-2], l[-2][0])
# ll = l[3: -2]
# print(ll)
# ll = l[3: -2: 3]
# print(ll)

# a = [1,2,3]
# b = [4,5,6]
# l = [a, b, 7, 8, 9]
# print(l)
# ll = l + l 
# print(ll)
# ll[0] = 100
# print(ll)
# ll[1].append(1000)
# print(ll)

# l = [1, 2, 3, 4, 5] * 3
# print(l)
# l = [[]*3]*3
# print(l)
# l[0].append(100)
# print(l)
# l[1].append(200)
# print(l)
# l = []
# for i in range(3):
#     l.append([])
# print(l) 
# l[0].append(100)
# print(l)

# l = [[]*3]*3
# print(l)
# l[1].append(100)
# print(l)

# l = [1,2,3]
# print(l)
# l.append(l)
# l.append(l)
# print(l)
# print(l[3])
# l[3][3][3][3][3][3][3][3][3][3][3][1] = 100
# s = [4,5,6]
# l.append(s)
# print(l)
# s[0] = 200
# print(l)
# print(id(l))
# print(id(l[3]))
# print(l[3][2])
   
# l = [1,2,3 , [4,5,6],"7, 8, 9"]
# print(1 in l)
# print(4 in l)
# print([4,5,6] in l)

# print(dir())
# print(dir(list))
# print([method for method in dir(list) if not method.startswith("_")])

# l = []
# print(l)
# l.append(1)
# print(l)
# l.append([1,2,3,4])
# l.append("test")
# print(l)
# # print(dir())
# l.extend([5,6,7])
# l.extend("test")
# print(l)
# l.insert(1, 100)
# print(l)
# print(l.count(1))
# print(l.count(100))
# print(l.count(1000))
# print(l.count([1, 2, 3, 4]))
# print(len(l))
# print(l.__len__())
# e = l.pop()
# print(l, e)
# e = l.pop(2)
# print(l, e)
# l.append(100)
# print(l)
# l.remove(100)
# print(l)
# # l.remove(1000) #ValueError: list.remove(x): x not in 
# # while 100 in l:
# #     l.remove(100)
# # l.remove(5, 6)#TypeError: list.remove() takes exactly one argument (2 given)
# l.insert(3, 100) 
# print(l)

# print(l.index(100))
# # print(l.index(-100))#ValueError: -100 is not in list
# print(l.index(100, 4)) #start from index 4
# # print(l.index(100, 4, 8)) #start from index 4 to 8
# # print(l.index(100, 4, 10)) #start from index 4 to 10

# l = [1,2,3,4,5]
# print(id(l), l)
# l.clear()
# print(id(l), l)
# l = []
# print(id(l), l)

# a = [1,2,3,4,5]
# l = [1,2,3,4,5, a]
# b = l.copy()
# print(id(l), l)
# print(id(b), b)
# print(l is b)
# print(l == b)
# a[0] = 100
# b[0] = 300
# b[5][3] = 300
# print(id(l), l)
# print(id(b), b)
# print("=="*20)
# from copy import deepcopy
# d = deepcopy(l)
# print(id(l), l)
# print(id(b), b)
# print(id(d), d)
# print("=="*20)
# a[2] = 200
# print(id(l), l)
# print(id(b), b)
# print(id(d), d)
# l.reverse()
# print(id(l), l)
# l.sort()
# l = [1,4,67,324,6,758,98,982,3,4,5]
# l.sort()
# print(id(l), l)
# l.sort(reverse=True)

# l = [1,2,35]
# print(all(l))
# l = [1,2,35, ""]
# print(all(l))
# print(any(l))

# l = [1,4,67,324,6,758,98,982,3,4,5]
# l.sort()
# print(id(l), l)
# ll = sorted(l, reverse=True)
# print(l)
# print(ll)



## tuple

# t = tuple()
# print(type(t), t)
# t = tuple("jdsfkd g")
# print(type(t), t)
# t = ()
# print(type(t), t)
# t = ("jdsfkd g", 1, 2.0, True)
# print(type(t), t)
# t = (123)
# print(type(t), t)
# t = (123,)
# print(type(t), t)
# print([method for method in dir(tuple) if not method.startswith("_")])
# from random import randint
# n = 10
# l = [randint(1, 100) for i in range(n)]
# t = tuple(l)
# print(f"list: {l} size: {len(l)} sizeof: {l.__sizeof__()}")
# print(f"tuple: {t} size: {len(t)} sizeof: {t.__sizeof__()}")

# n = 1000
# l = [randint(1, 100) for i in range(n)]
# t = tuple(l)
# print(f"list: size: {len(l)} sizeof: {l.__sizeof__()}")
# print(f"tuple:  size: {len(t)} sizeof: {t.__sizeof__()}")

# #set
# s = set()
# print(type(s), s)
# s = set("hello")
# print(type(s), s)
# # s = {} #<class 'dict'> {}
# s = {1, 2, 3, 4, 5, 5, 5, 5, 5}
# print(type(s), s)
# # s = {1, 2, []} #TypeError: unhashable type: 'list'
# print([method for method in dir(set) if not method.startswith("_")])
# s.add(100)
# print(s)
# print(s.pop())
# print(s)

# # text = "hello world"
# # s = set(text)
# # d = {}
# # while s:
# #     c = s.pop()
# #     d[c] = text.count(c)
# # print(d)

# s.add(True)
# s.add((1,2,3))
# print(s)

# # # s = set('foo', 35, True) #TypeError: set expected at most 1 argument, got 3
# # s = {'foo', 35, True}
# # print(s)

# s.update((4,5,6,7))
# print(s)


# ##dict
# d = dict()
# print(type(d), d)
# d = dict([(1,1), ("a", 2), (False, 4)])
# print(type(d), d)
# d = {}
# print(type(d), d)
# d = {
#     1: 1,
#     "a": 2,
#     False: 4,
#     (1,2): 5
# }
# print(type(d), d)
# print(d[(1,2)])
# # print(d[15]) #KeyError: 15
# print(d.get((1,2))) 
# print(d.get(15)) #None
# print(d.get(15, "GOO")) #None


print([method for method in dir(dict) if not method.startswith("_")])
d = {
    1: 1,
    "a": 2,
    False: 4,
    (1,2): 5
}

# d.update({1: 100, 2: 200})
# print(d)
# # dd = d.fromkeys([1,2,3], 100)
# # print(dd)
# print(d.popitem(), d)

# print(d.pop(1), d)
# print(d.keys())
# print(d.values())
# print(d.items())

# for key in d:
#     print(key, d[key])
# for key, value in d.items():
#     print(key, value)

# keys = [k for k in d.keys() if type(k) in (int, str)]
# print(keys)
# for key in keys:
#     print(key, d[key])


# l = []
# for i in range(1, 100):
#     if i % 2:
#         l.append(i)
# print(l)

# ll = [i*2 for i in range(1, 100) if i % 2]
# print(ll)

# l = []
# for i in range(1, 5):
#     for j in range(1, i):
#         if i+j >2:
#             l.append([i, j, i*j])
# print(l)

# ll = [[i, j, i*j] for i in range(1, 5) for j in range(1, i) if i+j >2]
# print(ll)

# print(tuple.__hash__)
# print(list.__hash__)

l = [1, [], "aa", set(), 1., True]

from collections.abc import Iterable

for t in l:
    # print(f"{type(t)} is iterable {isinstance(t, Iterable)}")