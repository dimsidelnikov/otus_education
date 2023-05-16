from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a_side, b_side):
        self.name = 'Rectangle'
        self.a_side = a_side
        self.b_side = b_side
        self.check_possible_create_rectangle(a_side, b_side)

    @property
    def perimeter(self):
        return (self.a_side + self.b_side) * 2

    @property
    def area(self):
        return self.a_side * self.b_side

    @staticmethod
    def check_possible_create_rectangle(a_side, b_side):
        if type(a_side) != int or type(b_side) != int:
            raise ValueError(f'Sides must be integer. Got: {a_side}: {type(a_side)}; {b_side}: {type(b_side)}')

        if not (a_side > 0 and b_side > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {a_side}, {b_side}')
