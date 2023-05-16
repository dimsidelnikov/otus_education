from src.figure import Figure


class Square(Figure):
    def __init__(self, a_side):
        self.name = 'Square'
        self.a_side = a_side
        self.check_possible_create_square(a_side)

    @property
    def perimeter(self):
        return self.a_side * 4

    @property
    def area(self):
        return self.a_side ** 2

    @staticmethod
    def check_possible_create_square(a_side):
        if type(a_side) != int:
            raise ValueError(f'Side must be integer. Got: {a_side}: {type(a_side)}')

        if not a_side > 0:
            raise ValueError(f'Side must be greater than 0. Got: {a_side}')
