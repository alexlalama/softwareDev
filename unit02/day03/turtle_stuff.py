import turtle
angle = 45
def test_drive():
    turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(120)
    turtle.penup()
    return "poop"
def turtle_state():
    """
    prints current state of turtle
    """
    return turtle.isdown(), turtle.heading(), turtle.xcor(), turtle.ycor()


def square(size, angle, pencolor, fillcolor):
    turtle.pensize(5)
    turtle.bgcolor("yellow")
    turtle.color(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.left(angle)
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.right(angle)
    turtle.penup()
    turtle.end_fill()
def main():
    # print(turtle_state())
    # test_drive()
    # print(turtle_state())
    print(turtle_state())
    square(120,95, "orange", "gray")
    print(turtle_state())
    

    print(turtle_state())
    square(90, 100, "green", "purple")
    print(turtle_state())

    print(turtle_state())
    square(50, 105, "red", "pink")
    print(turtle_state())
   
    input("Press enter to continue... ")
    
main()