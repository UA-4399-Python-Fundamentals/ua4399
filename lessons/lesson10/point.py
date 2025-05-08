class Point:
    def __init__(self, x, y):
        print(f"creating a point {x}, {y}")
        self.x = x
        self.y = y

    # def __del__(self):
    #     print(f"deleting a point {self.x}, {self.y}")
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # def __repr__(self):
    #     return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, int):
            print(f"adding {self} and {other}")
            return Point(self.x + other, self.y + other)
        elif isinstance(other, Point):
            print(f"adding {self} and {other}")
            return Point(self.x + other.x, self.y + other.y)

    def __len_to_zero__(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __lt__(self, other):
        return self.__len_to_zero__() < other.__len_to_zero__()

    def p2p(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


def f():
    print("function f called")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    return p2

if __name__ == "__main__":
    
    p1 = Point(10, 2)
    p4 = f()
    del p4
    p2 = Point(3, 4)
    p3 = Point(5, 6)

    print(p1, p2, p3)
    print([p1, p2, p3])
    p5 = p1 + p2
    print(p5)
    p6 = p1 + 10
    print(p6)

    l = [p1, p2, p3]
    print(l)
    l.sort()
    print(l)
    print(l[0].p2p(l[-1]))
