"""
    Author:Arvin Shaffer
    Function:Draw a five-pointed star!
    Version:2.0
    Date:02/13/2018
    2.0 New Function:Draw plots of different sizes
"""
import turtle

def draw_pentagram(size):
    """"
        Draw a five-pointed star!
    """
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1

def main():

    #turtle.backward(100)
    #use loop to draw
    turtle.penup()
    turtle.bk(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')
    size = 50
    while size <= 100:
        draw_pentagram(size)
        size += 10

    turtle.exitonclick()

if __name__ == "__main__" :
    main()
