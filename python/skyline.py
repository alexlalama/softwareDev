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
    turtle.pencolor(pen_color)
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

def equil_triangle(x_cor, y_cor, size, pen_color, fill_color):
    turtle.penup()
    turtle.goto(x_cor, y_cor)
    turtle.begin_fill()
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.pencolor(pen_color)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)  
    turtle.forward(size)
    turtle.left(120)
    turtle.end_fill() 

def draw_circle(x_cor, y_cor, radius, pen_color, fill_color):
     turtle.fillcolor(fill_color)
     turtle.color(pen_color)
     turtle.penup()
     turtle.goto(x_cor,y_cor)
     turtle.begin_fill()
     turtle.circle(radius)
     turtle.end_fill()
def main():
    rectangle(-340,-280,672, 150, "black", "green")
    
    rectangle(-340,-130,672, 800, "black", "magenta")
    rectangle(-300, -130,  150, 100,"brown", "brown")
    rectangle(-300, -30,  150, 50,"gray", "gray")
    equil_triangle(-220, -30, 70, "black", "brown")

    

    rectangle(-100, -130,  150, 100,"black", "pink")
    rectangle(-100, -30,  150, 50,"gray", "gray")
    equil_triangle(-20, -30, 70, "black", "pink")

    rectangle(100, -130,  150, 100,"black", "cyan")
    rectangle(100, -30,  150, 50,"gray", "gray")
    equil_triangle(180,-30, 70, "black", "cyan")
    draw_circle(-300, 190, 25, "yellow", "gray")
    input("Press enter to exit program...")

main()