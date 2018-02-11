"""
    Author:Arvin Shaffer
    Function:Draw a five-pointed star!
    Version:1.0
    Date:02/11/2018
"""
import turtle

def main():

    #turtle.backward(100)
    #use loop to draw
    count = 1
    while count <= 5:
        turtle.forward(200)
        turtle.right(144)
        count = count + 1

    #draw a five-pointed star
    #the first side
    # turtle.forward(100)
    # turtle.right(144)
    # #the seconde side
    # turtle.forward(100)
    # turtle.right(144)
    # #the third side
    # turtle.forward(100)
    # turtle.right(144)
    # #the fourth side
    # turtle.forward(100)
    # turtle.right(144)
    # #the fifth side
    # turtle.forward(100)
    # turtle.right(144)

    turtle.exitonclick()

if __name__ == "__main__" :
    main()
