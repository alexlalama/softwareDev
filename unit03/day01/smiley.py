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

def draw_centered_circle(x, y,radius,fillcolor):
    # use x, y
    # go to x + radius
    turtle.penup()
    turtle.goto(x,y)
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

def draw_smiley(x,y, radius, head_fill_color, nose_fill_color, mouth_fill_color):
    draw_centered_circle(x,y,radius, head_fill_color)
    draw_centered_circle(x,y,radius*.10, nose_fill_color)
    draw_eye(radius*.35, radius*.25,radius*.25,"brown")
    draw_eye(-1*(radius*.35), radius*.25,radius*.25,"brown")
    draw_mouth(x, y, radius, mouth_fill_color)
def tweak(speed,tracer):
    turtle.speed(speed)
    turtle.tracer(tracer)

def draw_eye(x, y, radius, iris_color):
    draw_circle(x, y, radius, "white")
    draw_circle(x, y+radius/2, radius/2, iris_color)
    draw_circle(x, y*2,radius/4, "black")

def draw_mouth(x, y, radius, fill_color):
    radius = radius *.6
    y = -1*(radius*.25)
    turtle.goto(x, y)
    turtle.forward(radius)
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
    # turtle.tracer(False)
    tweak(10,False)
    draw_smiley(0,0, 100, "yellow", "pink","black")
    input("Press enter to continue")

main()