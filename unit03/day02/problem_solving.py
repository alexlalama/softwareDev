"""
problem solving
alex lalama
"""
import turtle
import random

def random_location():
    turtle.pendown()
    turtle.goto(random.randint(-300, 300),random.randint(-300, 300))
    turtle.penup()

def random_number_location():
    """
    return a random number between .5 to 1.0
    """
    return 0

def random_angle():
    """
    moves turtle to a random angle
    """
    angle = random.randint(1 , 359)
    turtle.pendown()
    turtle.left(angle)
    print(angle)
    turtle.penup()

def turtle_color_red():
    """
    turns turtle color and fill color to red 
    """
    random_color = random.random()
    turtle.color(random_color, 0, 0)
    turtle.fillcolor(random_color, 0, 0)
def turtle_purple_color():
    """
    turns turtle color and fill color to purple 
    """
    random_color = random.random()
    turtle.color(random_color, 0, random_color)
    turtle.fillcolor(random_color, 0, random_color)
def random_colors():
    turtle.color(random.random(), random.random(), random.random())

def main():
    # random_location()
    # random_number_location()
    random_colors()
    random_angle()
    input("Press enter to continue")
main()