"""
    Author:Arvin Shaffer
    Function:Draw a five-pointed star!
    Version:3.1
    Date:02/14/2018
    3.1 New Function:Use iteration function draw plots of different sizes with my thinking
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

def draw_recursive_pentagram(size):
    """
    Use iteration to draw a five-pointed star
    :param size:
    :return:
    """
    #use function to draw
    draw_pentagram(size)
    #update the value of size
    size += 10
    if size <=100 :
        draw_recursive_pentagram(size)

def main():
    turtle.penup()
    turtle.bk(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50
    draw_recursive_pentagram(size)

    turtle.exitonclick()

if __name__ == "__main__" :
    main()
