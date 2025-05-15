"""
Program to draw a smile
Alexandra Lalama
"""
import turtle
def draw_circle(x_cor, y_cor, radius, fill_color):
    turtle.penup()
    turtle.goto(x_cor,y_cor)
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.circle(radius)
    turtle.end_fill()

def main():
    draw_circle(30, 40, 70, "magenta")
    input("Press enter to continue")
main()

