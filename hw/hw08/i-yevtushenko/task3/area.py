def rectalgle_area():
    a = int(input('a = '))
    b = int(input('b = '))
    return a * b

def triangle_area():
    H = int(input('H = '))
    B = int(input('B = '))
    return 1/2 * H * B

def circle_area():
    import math
    R = int(input('R = '))
    return math.pi * pow(R, R)

def select_formula():
    print("Select formula:")
    print("1. Rectangle area")
    print("2. Triange area")
    print("3. Circle area")
    print("4. Exit")
    s = int(input())
    if s == 1:
        print(rectalgle_area())
    elif s == 2:
        print(triangle_area())
    elif s == 3:
        print(circle_area())
    elif s == 4:
        print("Exit")  
    else:
        print('Wrong select, try again:')
        select_formula()