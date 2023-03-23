from random import random, choice

from tqdm import tqdm

import matplotlib.pyplot as plt

from math import sqrt

from dataclasses import dataclass

n = 100000

red_x = []
red_y = []
blue_x = []
blue_y = []

@dataclass
class Position:
    x: float
    y: float

def aire_rectangle(rectangle):
    l = sqrt((rectangle[0].x-rectangle[1].x)**2+(rectangle[0].y-rectangle[1].y)**2)
    L = sqrt((rectangle[1].x-rectangle[2].x)**2+(rectangle[1].y-rectangle[2].y)**2)
    return l*L

def aire_triangle(p1, p2, p3):
    return abs((p1.x*(p2.y-p3.y)+(p2.x*(p3.y-p1.y))+(p3.x*(p1.y-p2.y)))/2.0)

def point_dans_triangle(triangle, point):
    A = aire_triangle(triangle[0], triangle[1], triangle[2])
    A1 = aire_triangle(triangle[0], triangle[1], point)
    A2 = aire_triangle(triangle[0], triangle[2], point)
    A3 = aire_triangle(triangle[1], triangle[2], point)
    A_calc = A1 + A2 + A3
    return A_calc == A or abs(A_calc-A) <= 1e-3

p_A = Position(0, 7)
p_B = Position(14, 3)
p_C = Position(1, 0)
figure = (p_A, p_B, p_C)

x_min = min([point.x for point in figure])
x_max = max([point.x for point in figure])
y_max = max([point.y for point in figure])
y_min = min([point.y for point in figure])
rectangle = (Position(x_min, y_max), Position(x_max, y_max), Position(x_max, y_min), Position(x_min, y_min))
aire = aire_rectangle(rectangle)

for i in tqdm(range(n)):
    x = x_max*random()
    y = y_max*random()

    if point_dans_triangle(figure, Position(x, y)):
        red_x.append(x)
        red_y.append(y)
    else:
        blue_x.append(x)
        blue_y.append(y)

size = len(red_x)/n
print(size)


plt.scatter(blue_x, blue_y, color="blue")
plt.show()
