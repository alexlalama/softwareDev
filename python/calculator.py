def add(x, y):
    """
    Add function to add (2) numeric operands
    """
    sum = x +y
    return sum
def subtract(x, y):
    """
    subtraction function to subtract (2) numeric operands
    """
    subtract = x -y
    return subtract
def multiply(x, y):
    """
    multiply function to multiply (2) numeric operands
    """
    product = x *y
    return product
def divide(x, y):
    """
    divide function to divide (2) numeric operands
    """
    quiotent = x /y
    return quiotent

def main():
    x =int(input("Enter x: "))
    y =int(input("Enter y: "))

    print(add(x,y))
    print(subtract(x,y))
    print(multiply(x,y))
    print(divide(x,y))

main()