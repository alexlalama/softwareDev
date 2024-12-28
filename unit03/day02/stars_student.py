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
    turtle.goto(random.randint(-200, 200), random.randint(-200, 200)) 

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

    turtle.end_fill()    
def random_star(length):
    '''
    Draws a star at a random location, orientation, and length 
    '''
    random_move()
    draw_star(length)
def main():
    """
    Should ultimately draw a night sky filled with stars and planets.
    """
    turtle.bgcolor("black")
    tweak(1, True)
    '''
    Type Error
    Missing a cast from string to int
    VS code showed me the error
    '''
    length = int(input("Enter length of star to draw between 5 - 10: "))
    # draw_star(length)
    tweak(1, True)
    '''
    Runtime Error or Attribute Error
    Changed Tracer to false to hide turtle
    VS tracedback the error

    ''' 
    random_star(length)
    input("Press enter to continue...")

main()