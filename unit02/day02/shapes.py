"""
Program that has shape equations
Alex L
"""

def area_of_circle():
    """
    Calculates the area of a circle
    """
    radius = float(input("Enter a radius: ")) # Prompts for a radius
    area = float(3.14159 * (radius**2)) # Area equation
    print("Circle: r = ", radius, ", area = ", area, sep="")

def volume_of_sphere():
    """
    Calculates the volume of a sphere
    """
    radius = float(input("Enter a radius: ")) # Prompts for a radius
    volume = 4/3 * 3.14159 * (radius **3)
    print("Sphere: r = ", radius, ", volume = ", volume, sep="")

def area_of_rectangle():
    """
    Calculates the area of a rectangle
    """
    height = float(input("Enter a height: ")) # Prompts for a height
    width = float(input("Enter a width: ")) # Prompts for a width
    area = height * width # Area equation
    print("rectangle: height = ", height, ", width = ", width,", area = ", area, sep="")

def area_of_square():
    """
    Calculates the area of a square
    """
    side_length = float(input("Enter a side length: ")) # Prompts for a side length
    area = side_length * side_length # Area equation
    print("Square: side length = ", side_length, ", area: ", area, sep="")

def area_of_iso_triangle():
    """
    Calculates the area of a isosceles triangle
    """
    side = float(input("Enter a side: ")) # Prompts for a side
    height = float(input("Enter a height: ")) # Prompts for a height
    base = (((side**2)-(height**2))//3)*2
    area = (base*height)/2
    print("Isoscele Triangle: side = ",side, " ,height = ", height, " ,area = ",area,sep="")


def area_of_equilateral_triangle():
    """
    Calculates the area of a equilateral triangle
    """
    side = float(input("Enter a side: ")) # Prompts for a side
    area = (((3/2)/4)* (side**2))
    print("Equilateral Triangle: side = ", side, ", area = ", area, sep="")



def area_of_trapezoid():
    """
    Calculates the area of a trapezoid 
    """
    base1 = float(input("Enter a base: ")) # Prompts for a base
    base2 = float(input("Enter a base: ")) # Prompts for a base 
    height = float(input("Enter a height: ")) # Prompts for a height
    area = ((base1 + base2)/2)*height
    print("Area: ", area)



def main():
    area_of_circle()
    volume_of_sphere()
    area_of_rectangle()
    area_of_square()
    area_of_iso_triangle()
    area_of_equilateral_triangle()
    area_of_trapezoid()
main()