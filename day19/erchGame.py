import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(5)


def turn_right():
    tim.right(5)


def clear():
    screen.clear()


screen.listen()

screen.onkey(key='w' or 'W', fun=move_forwards)
screen.onkey(key='s' or 'S', fun=move_backwards)
screen.onkey(key='a' or 'A', fun=turn_left)
screen.onkey(key='d' or 'D', fun=turn_right)
screen.onkey(key='c' or 'C', fun=clear)

screen.exitonclick()
