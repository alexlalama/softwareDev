import turtle
import pixart
def test_speed():
    assert pixart.speed() == 0

def test_xcor():
    assert pixart.xcor() == -300


def test_ycor():
    assert pixart.ycor() == 300


def test_isdown():
    assert pixart.isdown() == False

def test_pencolor():
    assert pixart.pencolor() == 'black'

def test_fillcolor():
    assert pixart.fillcolor ()== 'white'
