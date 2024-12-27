"""
problem solving
alex lalama
"""
import turtle
import random

def random_location():
    turtle.pendown()
    turtle.goto(random.randint(-300, 300),random.randint(-300, 300))
    turtle.penup()
def main():
    random_location()
    input("Press enter to continue")
main()