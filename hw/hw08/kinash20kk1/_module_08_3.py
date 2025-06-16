#from math import pow, pi

def rectangle_area(l, w):
    area = l * w
    return round(area, 2)
def triangle_area(b, h):
    area = 1/2 * b * h
    return round(area, 2)
#def circle_area(r):
def circle_area(fun, pi):
    #area = pi * pow(r, 2)
    area = pi * fun
    return round(area, 2)