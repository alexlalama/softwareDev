import turtle

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
    if turtle.isdown():
        return True
    else:
        return False, turtle.heading(), turtle.xcor(), turtle.ycor()


def square():
    turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.penup()
def main():
    # print(turtle_state())
    # test_drive()
    # print(turtle_state())
    print(turtle_state())
    square()
    print(turtle_state())
    input("Press enter to continue... ")
    
main()