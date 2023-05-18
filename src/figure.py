from abc import ABC, abstractmethod


class Figure(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return round(self.area + figure.area, 2)
        raise ValueError(f'Object {figure} is not subclass of Figure class')
