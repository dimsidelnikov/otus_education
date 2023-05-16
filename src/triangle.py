import math
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a_side, b_side, c_side):
        self.name = 'Triangle'
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side
        self.check_possible_create_triangle(a_side, b_side, c_side)

    @property
    def perimeter(self):
        return self.a_side + self.b_side + self.c_side

    @property
    def area(self):
        half_perimeter = self.perimeter / 2
        return round(math.sqrt(half_perimeter *
                               (half_perimeter - self.a_side) *
                               (half_perimeter - self.b_side) *
                               (half_perimeter - self.c_side)), 2)

    @staticmethod
    def check_possible_create_triangle(a_side, b_side, c_side):
        if type(a_side) != int or type(b_side) != int or type(c_side) != int:
            raise ValueError(f'Sides must be integer. Got: {a_side}: {type(a_side)}; '
                             f'{b_side}: {type(b_side)}; '
                             f'{c_side}: {type(c_side)}')

        if not (a_side > 0 and b_side > 0 and c_side > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {a_side}, {b_side}, {c_side}')

        if not (a_side + b_side > c_side and a_side + c_side > b_side and c_side + b_side > a_side):
            raise ValueError(f'Sum of any two sides must be greater than thirds: {a_side}, {b_side}, {c_side}')
