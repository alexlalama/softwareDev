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

def main():
    num1 = int(input("Enter x: "))
    num2 = int(input("Enter y: "))
    print(add(num1, num2))
    print(subtract(num1, num2))
    print(multiply(num1, num2))
    print(divide(num1, num2))

main()