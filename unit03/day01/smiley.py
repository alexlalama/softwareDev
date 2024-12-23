"""
Drawing a smiley face

"""

import turtle
def draw_circle(x_cor, y_cor, radius,fillcolor):
    turtle.penup()
    turtle.setx(x_cor)
    turtle.sety(y_cor)
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.end_fill()

def draw_centered_circle(radius,fillcolor):
    # use x, y
    # go to x + radius
    turtle.penup()
    turtle.goto(0,0)
    turtle.forward(radius)
    turtle.left(90)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.fillcolor(fillcolor)
    turtle.penup()
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(radius)
    turtle.left(180)

def draw_smiley():
    draw_centered_circle(150, "yellow")
    draw_centered_circle(20, "pink")

def tweak(speed,tracer):
    turtle.speed(speed)
    turtle.tracer(tracer)

def draw_eye(x, y, radius, iris_color):
    draw_circle(x, y, radius, "white")
    draw_circle(x, y+radius/2, radius/2, iris_color)
    draw_circle(x, y*2,radius/4, "black")

def draw_mouth(x, y, radius, fill_color):
    turtle.goto(x,y)
    turtle.left(90)
    turtle.begin_fill()
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.circle(radius, -180)
    turtle.left(90)
    turtle.forward(radius)
    turtle.penup()
    turtle.end_fill()
def main():
    turtle.speed(10)
    draw_smiley()
    draw_eye(60, 30, 40, "brown")
    draw_eye(-60, 30, 40, "brown")
    draw_mouth(40,-60, 40, "black")
    input("Press enter to continue")

main()