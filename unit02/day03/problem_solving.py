import turtle
def draw_circle(x_cor, y_cor, radius, pencolor, fillcolor):
    turtle.penup()
    turtle.pensize(5)
    turtle.pencolor(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.setx(x_cor)
    turtle.sety(y_cor)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.end_fill()
    return print(turtle.isdown(), turtle.heading(), turtle.xcor(), turtle.ycor()) # state of the turtle
def main():
    draw_circle(20, 30, 50, "yellow", "purple")
    input("Press enter to continue")
main()