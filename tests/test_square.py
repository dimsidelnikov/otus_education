import pytest
from src.square import Square


@pytest.mark.parametrize('a_side, expected_perimeter, expected_area',
                         [
                             (5, 20, 25)
                         ])
def test_positive_create_square(a_side, expected_perimeter, expected_area):
    square = Square(a_side)
    assert square.name == 'Square', 'Correct name is Square'
    assert square.perimeter == expected_perimeter, f'Correct perimeter is {expected_perimeter}'
    assert square.area == expected_area, f'Correct area is {expected_area}'


@pytest.mark.parametrize('a_side', ['a_side', 0, -5], ids=['side is str', 'side is zero', 'side is negative'])
def test_negative_create_square(a_side):
    with pytest.raises(ValueError):
        Square(a_side)


def test_sum_two_square_areas():
    expected_sum = 125
    square_1 = Square(5)
    square_2 = Square(10)
    assert square_1.add_area(square_2) == expected_sum, f'Correct sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [5, 'square', [1, 'two']], ids=['integer', 'str', 'list'])
def test_negative_sum_two_square_areas(some_other_class):
    square_1 = Square(5)
    with pytest.raises(ValueError):
        square_1.add_area(some_other_class)
