import turtle
def convert_height():
    '''
    convert height from inch to feet and inches
    '''
    height = int(input("Enter your height in inches: "))
    feet = (height//12)
    inches = height%12
    print("You are ", feet ,"' ", inches," tall")


def convert_distance(kilometers):
    '''
    
    '''
    miles = 0
    feet = 0 
    inches = 0
    print(kilometers , " kilometers is " , miles , " miles" , feet, " feet, " , inches, " inches")

def snow_man(x, y, radius):
    
    turtle.goto(-330, -280)
    turtle.forward(280*2)
    turtle.left(90)
    turtle.forward(330*2)
    turtle.left(90)
    turtle.forward(280*2)
def main():
    x = 40
    y = 80
    radius = 30
    snow_man(x, y, radius)

main()