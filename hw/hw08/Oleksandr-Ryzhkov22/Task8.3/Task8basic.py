import math
def area_of_figures():
    area = input ("Enter the shape(circle, rectangle, triangle):")   
    if area == "circle":
        r = float(input("Enter the radius:"))
        print ((math.pi) * (math.pow(r , 2)))
    elif area == "rectangle":
        a = float(input("Enter the length:"))
        b = float(input("Enter the width:"))
        print (a * b)
    elif area == "triangle":
        a = float(input("Enter the base:"))
        b = float(input("Enter the height:"))
        print (0.5 * a * b)
    else:
        print ("Invalid shape")
    pass    
    
__all__ = [area_of_figures]    

area_of_figures()

    

    
  
    

