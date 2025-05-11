inp=input('what square do you want to calculate?(circle, rectangle, triangle):')

def sqr_circle(area):
    """
    Calculate the radius of a circle given its area.
    
    :param area: The area of the circle
    :print: The radius of the circle
    """
    inp1=input('value?:')
    area=int(inp1)
    print ((area/3.14159)**0.5)

def sqr_rectangle(area):   
    """
    Calculate the side length of a rectangle given its area.
    
    :param area: The area of the rectangle
    :print: The side length of the rectangle
    """
    inp1=input('value?:')
    area=int(inp1)
    print (area**0.5)

def sqr_triangle(area):
    """
    Calculate the base of an equilateral triangle given its area.
    
    :param area: The area of the triangle
    :print: The base of the triangle
    """
    inp1=input('value?:')
    area=int(inp1)
    print ((area*4/(3**0.5))**(1/3))

if inp=='circle':
    inp1=('value?:')
    sqr_circle(inp1)
elif inp == 'rectangle':
    inp1=('value?:')
    sqr_rectangle(inp1)
elif inp == 'triangle':
    inp1=('value?:')
    sqr_triangle(inp1)   



