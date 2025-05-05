#07.1
import random
x, y = random.randint(1, 1000), random.randint(1, 1000)
def return_larger(x, y):
    """This function compares two numbers and return largest one."""
    return max(x, y)
print(x, y)
print(return_larger.__doc__)
print("Largest is: ")
print(return_larger(x, y))

#07.2
import math
def rectangle():
    """Function 1 is for calculate rectangle's area by user input"""
    width_r = float(input("Type width of rectangle: "))
    height_r = float(input("Type height of rectangle: "))
    area_r = round((width_r*height_r), 2)
    return area_r
def triangle():
    """Function 2 is for calculate triangle's area by user input. 
    You must know lengths edge_1 and edge_2 and degree angle between them.
    Or you must know lenghts all three edges.
    """
    edge_1 = float(input("Type length of first edge: "))
    edge_2 = float (input("Type length of second edge: "))
    angle_1_2 = (input("*** \nType angle in degrees between edges: \nIf you don't know angle, then left free space and press Enter \n*** \n"))
    if angle_1_2:
        angle_1_2 = float(angle_1_2)
        if angle_1_2 < 180:
            pass
        else:
            print("That triangle don't exist. Reload program and check the input")
            return
        angle_rad = math.radians(angle_1_2)
        edge_3 = math.sqrt(edge_1**2 + edge_2**2 - 2 * edge_1 * edge_2 * math.cos(angle_rad))
        print(f"The third edge is approximately {edge_3:.3f}")
        area_t = 0.5 * edge_1 * edge_2 * math.sin(angle_rad)
        print(f"The area of the triangle is approximately {area_t:.3f}")
        return
    else:
        angle_1_2 =[]
        print("angle false \nUse Heron's formula to calculate triangle area.")
        edge_3 = float(input("Type length of third edge: \n"))
        #check 
        cos_1_2 = (edge_1**2+edge_2**2-edge_3**2)/(2*edge_1*edge_2)
        cos_1_2 = max(-1, min(1, cos_1_2))
        angle_1_2_rad = math.acos(cos_1_2)
        angle_1_2_deg = math.degrees(angle_1_2_rad)
        if angle_1_2_deg >= 180:
            print(f"The angle between first and second edges is approximately {angle_1_2_deg:.3f} degrees \nThat triangle don't exist. Reload program and check the input")
            return
        else:
            print("***")
            print(f"degree = {angle_1_2_deg:.3f} \n***")
        semi_perimeter = (edge_1+edge_2+edge_3) / 2
        area_t = math.sqrt(semi_perimeter*(semi_perimeter-edge_1)*(semi_perimeter-edge_2)*(semi_perimeter-edge_3))
        print(f"The area of the triangle is approximately {area_t:.3f}")
        return
#triangle()
def circle():
    """Function 3 is for calculate the circle's area by user input the radius. """
    radius_c = float(input("Type the circle's radius: "))
    area_c = round((math.pi * radius_c**2), 2)
    return area_c

def main():
    """Main function is managed user choce between functions for calculate areas of rectangle, triangle, circle."""
    progs = ["1", "2", "3"]
    user = input("This program can calculate areas of rectangle, triangle and circle. \n Type 1 for rectangle, 2 - for triangle and 3 - for circle. \n Press 1, 2, or 3: ")
    while user not in progs:
       print("Check the input. ")
       user = input("Type 1 for rectangle, 2 - for triangle and 3 - for circle: ")
    if user == '1':
        print(rectangle.__doc__)
        area_r = rectangle()
        print(f"Area of rectangle: {area_r}")
        return
    if user == '2':
        print(triangle.__doc__)
        triangle()
        return
    if user == '3':
        print(circle.__doc__)
        area_c = circle()
        print(f"Area of circle: {area_c}")
        return
main()

#07.3 calculate number of characters
def num_letter(s: str) -> dict:
    """***\nThis function calculate each letters in the string and return numbers of them.\n***"""
    out = {}
    for lett in s:
        out[lett] = out.get(lett, 0) + 1
    return out
print(num_letter.__doc__)
anystr = input("Type any text: ")
result = num_letter(anystr)
print(result)