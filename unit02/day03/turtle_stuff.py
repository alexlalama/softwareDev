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
    if turtle.isdown():
        return True
    else:
        return False, turtle.heading(), turtle.xcor(), turtle.ycor()


def square(size, angle):
    turtle.left(angle)
    turtle.pendown()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.right(45)
    turtle.penup()
def main():
    # print(turtle_state())
    # test_drive()
    # print(turtle_state())
    print(turtle_state())
    square(50,95)
    print(turtle_state())
    print(turtle_state())
    square(100, 100)
    print(turtle_state())
    print(turtle_state())
    square(150, 105)
    print(turtle_state())
   
    input("Press enter to continue... ")
    
main()