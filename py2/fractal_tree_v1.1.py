"""
    Author:Arvin Shaffer
    Function:Draw a five-pointed star!
    Version:1.1
    Date:02/15/2018
    1.1 New Function:Use iteration function draw Fractal tree
"""
import turtle

def draw_recursive_Fractal(size):
    """
    Use iteration to draw a Fractal tree
    :param size:
    :return:
    """
    if size > 5:
        turtle.forward(size)
        turtle.right(20)
        draw_recursive_Fractal(size - 10)
        turtle.left(40)
        draw_recursive_Fractal(size - 10)
        turtle.right(20)
        turtle.backward(size)

def initial_brush():
    turtle.pencolor('red')
    turtle.penup()
    turtle.sety(-100)
    turtle.pendown()
    turtle.left(90)

def main():
    initial_brush()
    draw_recursive_Fractal(66)
    turtle.exitonclick()

if __name__ == "__main__" :
    main()
