"""
Assignment 3.1
Alex Lalama
"""
import turtle
def convert_height(height):
    height = int(input("entre your height in inches: "))
    feet = height / 12
    inches = height % 12
    print (int(feet) , inches)

def convert_distance(kilometers):
    kilometers = float(input("Enter a distance in kilometers: "))
    inches = int(39370.1 * kilometers)    
    feet = int((kilometers*39370.1)/12)
    miles = int((39370.1*kilometers)/ 63360)
    feet1 = (miles/5280)
    print(miles, feet1,inches )
def snow_man(x,y,radius):
    turtle.fillcolor("white")
    turtle.pencolor("black")
    turtle.bgcolor("cyan")
    circle(x,y, radius)
    bottom_snowman(x, y, radius)
    small_snowman(x, y, radius)
def circle(x, y, radius):
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x,y)
    turtle.forward(radius)
    turtle.left(90)
    turtle.circle(radius)
    turtle.left(90)
    turtle.forward(radius)
    turtle.left(180)
    turtle.pendown()
    turtle.end_fill()
def bottom_snowman(x,y,radius):
    turtle.left(90)
    circle(x, radius+ radius*.75,radius*.75)

def small_snowman(x, y, radius):
    turtle.left(90)
    circle(x, radius+(radius*.75)*2+ (radius*.25)*2,(radius*.25)*2)
def main():
    # convert_height(71)
    # convert_distance(123.5)
    snow_man(0,0,40)
    input("press enter to continue")
main()

