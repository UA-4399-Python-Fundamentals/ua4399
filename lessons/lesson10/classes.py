class p:pass
class X(p):
    def x(self):
        print("x")
class Y(p): 
    def y(self):
        print("y")
class Z: 
    def z(self):
        print("z")
class A(X, Y): 
    def x(self):
        print("ax")
    def z(self):
        print("az")
class B(Y, Z): 
    def y(self):
        print("by") 
    def z(self):
        print("bz")
class M(B,A, Z): pass

m = M()
m.x()
m.y()
m.z()
print(M.__mro__)
