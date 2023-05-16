import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        self.name = 'Circle'
        self.radius = radius
        self.check_possible_create_circle(radius)

    @property
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    @property
    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    @staticmethod
    def check_possible_create_circle(radius):
        if type(radius) != int:
            raise ValueError(f'Radius must be integer. Got: {radius}: {type(radius)}')

        if not radius > 0:
            raise ValueError(f'Radius must be greater than 0. Got: {radius}')
