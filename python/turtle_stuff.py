import turtle
angle = 75
def test_drive():
    turtle.color("green")
    turtle.forward(100)
    turtle.left(57)
    turtle.setheading(127)
    turtle.circle(10)
    turtle.up()
def turtle_state():
    
    if(turtle.isdown() == True):
        return "true"
    if(turtle.isdown() == False):
        return "false"
    
    angle = turtle.heading()
    x_cor = turtle.xcor()
    y_cor = turtle.ycor()
    return angle, x_cor, y_cor


def square(size, angle, pencolor, fillcolor):
    """
    Draw a square
    """
    turtle.pensize(5)
    turtle.color(pencolor)
    turtle.bgcolor("red")
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.setheading(0)
    turtle.end_fill()

def draw_circle(x_cor, y_cor, radius, pen_color, fill_color):
     turtle.fillcolor(fill_color)
     turtle.color(pen_color)
     turtle.penup()
     turtle.goto(x_cor,y_cor)
     turtle.begin_fill()
     turtle.circle(radius)
     turtle.end_fill()   

def equil_triangle(x_cor, y_cor, size, pen_color, fill_color):
     turtle.penup()
     turtle.goto(x_cor, y_cor)
     turtle.begin_fill()
     turtle.pendown()
     turtle.fillcolor(fill_color)
     turtle.color(pen_color)
     turtle.forward(size)
     turtle.left(120)
     turtle.forward(size)
     turtle.left(120)  
     turtle.forward(size)
     turtle.left(120)
     turtle.end_fill()   
def rectangle(x_cor, y_cor, width, height, pen_color, fill_color):
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




def composite_shape(x_cor, y_cor,size,width, height, pen_color):
    turtle.penup()
    turtle.goto(x_cor, y_cor)
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
    turtle.goto(x_cor , y_cor + height)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.end_fill()


def main():
    print(turtle_state())
    '''
    square(100, 40, 'brown', 'pink')
    square(50, 24, 'yellow', 'green')
    square(30, 38, 'orange', 'purple')
    print(turtle_state())
    draw_circle(30, 40,20,'cyan','brown')
    equil_triangle(30, 40,20,'cyan','brown')
    '''
    # x_cor, y_cor, size,width, height, pen_color, fill_color
    composite_shape(30, 40,20,50,70 ,'brown')
    #rectangle(30, 40,20,50,'cyan','brown')
    input("Press enter to exit program...")
    
main()