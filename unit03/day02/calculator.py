"""
Activities for Unit 03 Day 2
Alex Lalama
"""
PI = 3.14159

def add(num1, num2):
    sum = num1 + num2
    return sum

def subtract(num1, num2):
    result = int(num1 - num2)
    return result
def multiply(num1, num2):
    result = int(num1 * num2)
    return result
def divide(num1, num2):
    result = float(num1 / num2)
    return result


def circumference(radius):
    """
    computes the circumference of a circle
    """
    circumference = 2*PI * radius
    return circumference

def area(radius):
    area = radius**2 *PI
    return area
def main():
    # num1 = int(input("Enter x: "))
    # num2 = int(input("Enter y: "))
    # print(add(num1, num2))
    # print(subtract(num1, num2))
    # print(multiply(num1, num2))
    # print(divide(num1, num2))
    radius = 10
    print("Radius: ", radius)
    print("Circumference: ", circumference(radius)) 
    print("Area: ", area(radius))

main()