import turtle

def test_drive():
    turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.home()
    turtle.penup()

def main():
    test_drive()
    input("Press enter to continue... ")
main()