import math
def area_r(length_r, heigth_r):
    length_r = float(length_r)
    heigth_r = float(heigth_r)
    s = length_r*heigth_r
    return s
def area_t (base_t, heigth_t):
    base_t = float(base_t)
    heigth_t = float(heigth_t)
    s = 0.5*base_t*heigth_t
    return s
def area_c (radius):
    radius = float(radius)
    s = math.pi*pow(radius, 2)
    return s
__all__ = ["area_r", "area_t", "area_c"]