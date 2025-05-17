"""
Program to draw a smile
Alexandra Lalama
"""
import turtle
def draw_circle(x_cor, y_cor, radius, fill_color):
    """
    draws a circle
    """
    turtle.speed(2)
    turtle.penup()
    turtle.goto(x_cor,y_cor)
    turtle.forward(radius)
    turtle.begin_fill()
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.circle(radius)
    turtle.end_fill()
    turtle.left(90)
    turtle.penup()
    turtle.forward(radius)
    turtle.left(180)


def draw_centered_circle(x, y, radius, fill_color):
    # turn 90 
    # forward radius
    # forward radius*.25
    # draw circle
    # turtle.penup()
    turtle.fillcolor(fill_color)
    # turtle.pendown()
    turtle.begin_fill()
    turtle.forward(radius*.25)
    turtle.penup()
    turtle.left(90)
    turtle.circle(radius*.25)
    turtle.end_fill()
    
def draw_smiley(x, y, radius, head, nose):
    draw_circle(x, y, radius, head)
    draw_centered_circle(x, y, radius, nose)

def tweak(speed, tracer):
    turtle.speed(speed)
    # turtle.tracer(tracer)
    
def draw_eye(x, y, radius, iris_color):
    draw_circle(x, y, radius, 'white')
    draw_circle(x, y, radius*.5,iris_color)
    draw_circle(x, y,radius*.25, 'black')

def main():
    x = 40
    y = 60
    radius = 80
    # tweak(3, False)
    # draw_eye(x, y, radius, 'green')
    # draw_circle(x,y,radius, 'gray')    
    # smiley(x, y, radius, 'blue', 'cyan')
    draw_smiley(x, y, radius, 'yellow', 'red')
    input("Press enter to continue")

main()

