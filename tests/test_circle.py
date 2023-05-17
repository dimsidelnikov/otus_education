import pytest
from src.circle import Circle


@pytest.mark.parametrize('radius, expected_perimeter, expected_area',
                         [
                             (5, 31.42, 78.54)
                         ])
def test_positive_create_circle(radius, expected_perimeter, expected_area):
    circle = Circle(radius)
    assert circle.name == 'Circle', 'Correct name is Circle'
    assert circle.perimeter == expected_perimeter, f'Correct perimeter is {expected_perimeter}'
    assert circle.area == expected_area, f'Correct area is {expected_area}'


@pytest.mark.parametrize('radius', ['radius', 0, -5], ids=['radius is str', 'radius is zero', 'radius is negative'])
def test_negative_create_circle(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_sum_two_circle_areas():
    expected_sum = 392.7
    circle_1 = Circle(5)
    circle_2 = Circle(10)
    assert circle_1.add_area(circle_2) == expected_sum, f'Correct sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [5, 'circle', [1, 'two']], ids=['integer', 'str', 'list'])
def test_negative_sum_two_circle_areas(some_other_class):
    circle_1 = Circle(5)
    with pytest.raises(ValueError):
        circle_1.add_area(some_other_class)
