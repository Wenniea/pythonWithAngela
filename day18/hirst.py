# This code will not work in repl.it as there is no access to the colorgram package here.###
# We talk about this in the video tutorials##
import colorgram
import turtle as t

tim = t.Turtle()  # Turtle is the class constructor to instantiate the class and turtle is the
# package

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
t.colormode(255)

# for color in colors:
# r = color.rgb.r
# g = color.rgb.g
# b = color.rgb.b
# new_color = (r, g, b)
# rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136),
              (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
              (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.pensize(20)
tim.speed(10)
tim.up()
tim.goto(-200, 200)  # so it shows the full 100 circles

for i in range(0, 100, 10):
    tim.down()
    for j in range(10):
        tim.down()
        new_color = color_list[(i + j) % 27]  # loops the color_list
        tim.dot(20, new_color)
        tim.up()
        tim.forward(40)
    tim.right(90)
    tim.up()
    tim.forward(40)
    tim.right(90)
    tim.forward(400)
    tim.right(180)

t.done()
