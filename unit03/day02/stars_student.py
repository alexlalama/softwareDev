"""
Draws a sky filled with stars and planets.

@Alex Lalama
"""

import random
import turtle

def tweak(speed, tracer):
    """
    Adjust the turtle's speed and tracer settings so that it can be sped up
    or slowed down as needed for visual debugging.
    """
    turtle.speed(speed)
    turtle.tracer(tracer)

def random_yellow():
    """
    Sets the turtle's fill color to a random shade of yellow using RGB values.
    """
    # the random.random() function returns a floating point value between
    # 0.1 and 1.0. This expression guarantees that the red value will be
    # between 0.5 and 1.0.
    red = 0.5 + random.random() * 0.5
    green = red
    blue = red / 2

    # the turtle color can be set using RGB values ranging from 0.0 to 1.0. In
    #  this case the red and green values are between 0.5 and 1.0 and the blue
    # value is half the value - this guarantees a shade of yellow.
    turtle.color(red, green, blue)
    turtle.fillcolor(red, blue, green)

def random_move():
    """
    Moves the turtle to a random location and orientation on the screen.
    """
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    turtle.goto(x, y) 

    angle = random.randint(0, 360)
    turtle.left(angle)


'''
Syntax Error
Missing ':' after function definition
VS showed the error
'''
def draw_star(length):
    """
    Draws a star at the turtle's current location and orientation.
    """
    random_yellow()

    turtle.down()
    turtle.begin_fill()

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.penup()
    turtle.end_fill()    
def random_star(length):
    '''
    Draws a star at a random location, orientation, and length 
    '''
    random_move()
    draw_star(length)

def draw_world(x, y, radius, fill_color):
    '''
    Draws a world
    '''
    turtle.goto(x, y)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    # turtle.forward(radius)
    # turtle.pendown()
    # turtle.left(90)
    turtle.circle(radius)
    turtle.penup()
    turtle.end_fill()

def draw_celestial_bodies():
    draw_world(-40,-80,60,"pink")
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    random_star(random.randint(5,10))
    draw_world(50, 80, 20, "red")
    draw_world(-80, 29, 90, "gray")
def main():
    """
    Should ultimately draw a night sky filled with stars and planets.
    """
    turtle.bgcolor("black")
    tweak(7, False)
    '''
    Type Error
    Missing a cast from string to int
    VS code showed me the error
    '''
    # length = int(input("Enter length of star to draw between 5 - 10: "))
    # # draw_star(length)
    # tweak(1, False)
    '''
    Runtime Error or Attribute Error
    Changed Tracer to false to hide turtle
    VS tracedback the error

    ''' 
    # random_star(length)
    # draw_world(70, 20, 80, "blue")
    
    draw_celestial_bodies()
    input("Press enter to continue...")
main()