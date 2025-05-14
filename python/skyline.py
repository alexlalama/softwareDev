"""
Using Turtle to draw a Skyline 
Alexandra Lalama
"""
import turtle

def rectangle(x_cor, y_cor, width, height, pen_color, fill_color):
    """
    Draws a rectangle
    """
    turtle.penup()
    turtle.goto(x_cor, y_cor)
    turtle.fillcolor(fill_color)
    turtle.color(pen_color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()   
