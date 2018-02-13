"""
    Author:Arvin Shaffer
    Function:Draw a five-pointed star!
    Version:1.1
    Date:02/12/2018
    1.1 New Function:
"""
import turtle

def draw(r):
    count = 1
    while count <= 5:
        turtle.forward(r)
        turtle.right(144)
        count += 1

def main():

    turtle.penup()
    turtle.bk(200)
    turtle.pendown()
    radius = 50
    i = 1
    while i <= 4:
        draw(radius)
        radius *= 2
        i += 1
    turtle.exitonclick()

if __name__ == "__main__" :
    main()
