from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, a_side):
        super().__init__(a_side, a_side)
        self.name = 'Square'
