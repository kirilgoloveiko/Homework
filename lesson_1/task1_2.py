import math


def circle_square_and_perimeter(radius):
    S = math.pi * radius ** 2
    P = 2 * math.pi * radius
    return f'Square = {round(S, 2)}, perimeter = {round(P, 2)}'


def square_square_and_perimeter(side):
    S = side ** 2
    P = 4 * side
    return f'Square = {round(S, 2)}, perimeter = {round(P, 2)}'
