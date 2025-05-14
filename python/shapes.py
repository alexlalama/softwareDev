"""
Calulate area and volume of shapes
"""
PI =355/113
def area_circle():
    """
    Area of a circle
    """
    radius = float(input("Enter a radius "))
    area = PI * (radius**2)
    print("Circle: r = ", radius, "area = ",area)

def volume_sphere():
    """
    Volume of a sphere
    """
    radius = float(input("Enter the radius: "))
    volume = (4/3)*(radius**3)*PI
    print("Sphere: r = ", radius, "volume = ", volume)

def area_rectangle():
    """
    Area of a rectangle
    """
    height = int(input("Enter the height: "))
    width = int(input("Enter the width: "))
    area = float(height *width)
    print("Rectangle: height = ", height, "width = ", area)

def area_square():
    """
    Area of a square
    """
    side_length = int(input("Enter the side length: ")) 
    area = float(side_length*2)
    print("Square: side length = ", side_length, "area = ", area)
    
def area_iso_triangle():
    """
    Area of isosceles triangle
    """
    side_length = int(input("Enter the side length: ")) 
    height = int(input("Enter the height: ")) 
    area= side_length * height/2
    print("Square: side length = ", side_length, "height = ", height , " area = ", area)

def area_equil_triangle():
    """
    Area of equilateral triangle
    """
    side_length = int(input("Enter the side length: "))
    area = (3**(1/2)/4)*side_length**2
    print(area)
    
def area_trapezoid():
    """
    Area of a trapezoid
    """
    base1 = int(input("Enter base 1: "))
    base2 = int(input("Enter base 2: "))
    height = int(input("Enter the height: "))
    area = ((base1 +base2)/2)*height
    print("Square: base1 = ", base1, "base1 = ", base2 , " height = ", height, " area = ", area)
def main():
    #area_circle()
    #volume_sphere()
    #area_equil_triangle()
    #area_square()
    area_iso_triangle()
    #area_trapezoid()
main()