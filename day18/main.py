# this imports everything
import random
import turtle as t

tim = t.Turtle()
colors = ["thistle", "light pink", "steel blue", "olive drab"]
directions = [0, 90, 180, 270]
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# dash lines - cmd + / to comment all selected
# for i in range(15):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# draw polygons with different color
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# random line with random color and speech
# for i in range(200):
#     if i > 50 & i < 100:
#         tim.speed(8)
#
#     if i > 100 & i < 150:
#         tim.speed(9)
#     if i > 150:
#         tim.speed(10)
#     tim.color(random.choice(colors))
#     tim.pensize(10)
#     tim.setheading(random.choice(directions))
#     tim.forward(30)

# using tuple
# for i in range(200):
#     if i > 50 & i < 100:
#         tim.speed(8)
#
#     if i > 100 & i < 150:
#         tim.speed(9)
#     if i > 150:
#         tim.speed(10)
#     tim.color(random_color())
#     tim.pensize(10)
#     tim.setheading(random.choice(directions))
#     tim.forward(30)


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

t.done()
