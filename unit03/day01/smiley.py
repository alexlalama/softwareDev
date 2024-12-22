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

def draw_centered_circle(x_cor, y_cor, radius,fillcolor):
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
    draw_centered_circle(100, 100, 150, "gray")
    draw_centered_circle(100, 100, 20, "pink")
def main():
    # draw_circle(20, 30, 59, "red")
    # draw_circle(200, 230, 10, "black")
    # draw_circle(100, 100, 70, "gray")
    draw_smiley(20, "pink")
    input("Press enter to continue")

main()