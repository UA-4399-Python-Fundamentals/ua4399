import math
def area_of_figures(area):
    area = input ("Enter the shape:")   
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
    
area_of_figures    
    

    
  
    

