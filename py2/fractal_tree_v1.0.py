"""
    Author:Arvin Shaffer
    Function:Draw a Fractal Tree!
    Version:1.0
    Date:02/15/2018
    1.0 New Function:Use iteration function draw Fractal tree
"""
import turtle

def draw_branch(branch_length):
    """
    draw fractal tree
    :return:
    """
    if branch_length >= 5:
        if branch_length <= 25:
            turtle.pencolor("green")
        else :
            turtle.pencolor("brown")
        #draw right branch
        turtle.forward(branch_length)
        print("forward:",branch_length)
        turtle.right(20)
        print("right 20.")
        draw_branch(branch_length - 15)

        #draw left branch
        turtle.left(40)
        print("left 0.")
        draw_branch(branch_length - 15)

        #Return to the previous branch
        turtle.right(20)
        print("right back 20")
        if branch_length <= 25:
            turtle.pencolor("green")
        else :
            turtle.pencolor("brown")
        turtle.backward(branch_length)


def initial_brush():
    turtle.pencolor('brown')
    turtle.penup()
    turtle.right(90)
    turtle.forward(200)
    turtle.pendown()
    turtle.left(180)


def main():
    initial_brush()
    draw_branch(100)
    turtle.exitonclick()

if __name__ == "__main__" :
    main()
