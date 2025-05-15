"""
Program to draw a smile
Alexandra Lalama
"""
import turtle
def draw_circle(x_cor, y_cor, radius, fill_color):
    """
    draws a circle
    """
    turtle.penup()
    turtle.goto(x_cor,y_cor)
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.circle(radius)
    turtle.end_fill()

def draw_centered_circle(x_cor, y_cor, radius):
    """
    draws a centered cirlce
    """
    # draw a circle
    # forward radius
    # turn forward radius
    draw_circle(x_cor, y_cor, radius,"purple")
    turtle.left(90)
    turtle.forward(radius)
    turtle.right(90)
def main():
    #draw_circle(30, 40, 70, "magenta")
    draw_centered_circle(39, 50, 70)
    input("Press enter to continue")

main()

