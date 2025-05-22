import math

def desc(a,b,c):
    return b**2 - 4 * a * c
def q2(a,b,c):
    d = desc(a,b,c)
    if d < 0:
        return 'No roots'
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        return (x1, x2) if x1 < x2 else (x2, x1)
        