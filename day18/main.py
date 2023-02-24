# import colorgram
# import turtle
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# color_num = 0
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [
    (118, 186, 169),
    (115, 160, 201),
    (215, 228, 238),
    (193, 136, 173),
    (236, 226, 206),
    (190, 219, 207),
    (206, 164, 107),
    (232, 209, 115),
    (73, 118, 158),
    (167, 206, 184),
    (115, 80, 117),
    (172, 98, 135),
    (101, 124, 177),
    (130, 85, 68),
    (234, 203, 213),
    (85, 155, 132),
    (228, 167, 184),
    (74, 129, 111),
    (66, 38, 47),
    (85, 52, 59),
    (176, 189, 212),
    (202, 75, 70),
    (157, 203, 218),
    (165, 133, 79),
    (219, 177, 172),
    (88, 53, 49),
    (31, 35, 52),
    (60, 43, 40),
    (54, 56, 94),
    (82, 144, 166)
]


import turtle
import random

turtle.colormode(255)

turtle.dot()
turtle.fd(50); turtle.dot(20, random.choice(color_list) ); turtle.fd(50)