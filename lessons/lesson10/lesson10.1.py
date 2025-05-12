# class ERT:
#     def __init__(self, a, b, c):
#         self.public = a
#         self._protected = b
#         self.__private = c
#     def __str__(self):
#         return f"ERT({self.public}, {self._protected}, {self.__private})"

# a = ERT(1,2,3)

# print(a.public)
# print(a._protected)
# # print(a.__private)  # This will raise an AttributeError
# print(a._ERT__private)  # This will work, but it's not recommended
# print(dir(a))
# print(a)


# class Point:
#     def __init__(self, x, y):
#         print(f"creating a point {x}, {y}")
#         if not isinstance(x, (int, float)):
#             print(f"x should be int or float, not {type(x)}")
#             self._x = 0
#         else:
#             self._x = x
#         if not isinstance(y, (int, float)):
#             print(f"y should be int or float, not {type(y)}")
#             self._y = 0
#         else:
            
#             self._y = y

#     def __str__(self): 
#         return f"Point({self._x}, {self._y})"
    
#     def get_x(self):
#         print(f"getting x: {self._x}")
#         return self._x
#     def set_x(self, x):
#         print(f"setting x: {x}")
#         if not isinstance(x, (int, float)):
#             print(f"x should be int or float, not {type(x)}")
#             return
#         self._x = x
#     x = property(get_x, set_x)

#     @property
#     def y(self):
#         print(f"getting y: {self._y}")
#         return self._y
    
#     @y.setter
#     def y(self, y):
#         print(f"setting y: {y}")
#         if not isinstance(y, (int, float)):
#             print(f"y should be int or float, not {type(y)}")
#             return
#         self._y = y

# p = Point(10, 20)
# # print(p)
# # p2 = Point("10", 20)
# # print(p2)

# # # p._x = "dsghkjdfnhklg"
# # # print(p)
# # p.set_x("dsghkjdfnhklg")
# # print(p)
# # print(p.get_x())
# p.x = 100
# print(p.x)
# print(p.y)
# p.y = "njhdbfjvfd"
# p.y = 200
# print(p)

class Point:
    def __init__(self, x, y):
        print(f"creating a point {x}, {y}")
        if not isinstance(x, (int, float)):
            print(f"x should be int or float, not {type(x)}")
            self._x = 0
        else:
            self._x = x
        if not isinstance(y, (int, float)):
            print(f"y should be int or float, not {type(y)}")
            self._y = 0
        else:
            self._y = y
    def __str__(self):
        return f"Point({self._x}, {self._y})"
    def add(self, other):
        if isinstance(other, int):
            print(f"adding {self} and {other}")
            return Point(self._x + other, self._y + other)
        elif isinstance(other, Point):
            print(f"adding {self} and {other}")
            return Point(self._x + other._x, self._y + other._y)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Point' and '{type(other)}'")
    def add(self, other, a):
        print(f"adding {self} and {other}")
        return Point(self._x * other._x, self._y * other._y)
    
        
p1 = Point(10, 20)
p2 = Point(30, 40)
p3 = p1.add(p2, 2)
print(p3)

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        print(f"creating a point {x}, {y}, {z}")
        if not isinstance(z, (int, float)):
            print(f"z should be int or float, not {type(z)}")
            self._z = 0
        else:
            self._z = z

    def __str__(self):
        return f"Point3D({self._x}, {self._y}, {self._z})"
    
p1 = Point3D(10, 20, 30)
p2 = Point3D(30, 40, 50)
p3 = p1.add(p2, 2)
print(p3)
print(p1)