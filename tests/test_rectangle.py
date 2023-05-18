import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize('a_side, b_side, expected_perimeter, expected_area',
                         [
                             (5, 10, 30, 50),
                             (5, 5, 20, 25)
                         ],
                         ids=[
                             'sides are not equal',
                             'sides are equal'
                         ])
def test_positive_create_rectangle(a_side, b_side, expected_perimeter, expected_area):
    rectangle = Rectangle(a_side, b_side)
    assert rectangle.name == 'Rectangle', 'Correct name is Rectangle'
    assert rectangle.perimeter == expected_perimeter, f'Correct perimeter is {expected_perimeter}'
    assert rectangle.area == expected_area, f'Correct area is {expected_area}'


@pytest.mark.parametrize('a_side, b_side',
                         [
                             (5, 'b_side'),
                             (0, 3),
                             (10, -5)
                         ],
                         ids=[
                             'one side is str',
                             'one side is zero',
                             'one side is negative'
                         ])
def test_negative_create_rectangle(a_side, b_side):
    with pytest.raises(ValueError):
        Rectangle(a_side, b_side)


def test_sum_two_rectangle_areas():
    expected_sum = 75
    rectangle_1 = Rectangle(5, 10)
    rectangle_2 = Rectangle(5, 5)
    assert rectangle_1.add_area(rectangle_2) == expected_sum, f'Correct sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [5, 'rectangle', [1, 'two']], ids=['integer', 'str', 'list'])
def test_negative_sum_two_rectangle_areas(some_other_class):
    rectangle_1 = Rectangle(5, 10)
    with pytest.raises(ValueError):
        rectangle_1.add_area(some_other_class)
